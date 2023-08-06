# Copyright © 2021 United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration.  All Rights Reserved.

from .. import PrognosticsModel
from numpy import maximum


class ThrownObject(PrognosticsModel):
    """
    Model that similates an object thrown into the air without air resistance

    Events (2)
        | falling: The object is falling
        | impact: The object has hit the ground

    Inputs/Loading: (0)

    States: (2)
        | x: Position in space (m)
        | v: Velocity in space (m/s)

    Outputs/Measurements: (1)
        | x: Position in space (m)

    Keyword Args
    ------------
        process_noise : Optional, float or Dict[Srt, float]
          Process noise (applied at dx/next_state). 
          Can be number (e.g., .2) applied to every state, a dictionary of values for each 
          state (e.g., {'x1': 0.2, 'x2': 0.3}), or a function (x) -> x
        process_noise_dist : Optional, String
          distribution for process noise (e.g., normal, uniform, triangular)
        measurement_noise : Optional, float or Dict[Srt, float]
          Measurement noise (applied in output eqn).
          Can be number (e.g., .2) applied to every output, a dictionary of values for each
          output (e.g., {'z1': 0.2, 'z2': 0.3}), or a function (z) -> z
        measurement_noise_dist : Optional, String
          distribution for measurement noise (e.g., normal, uniform, triangular)
        g : Optional, float
            Acceleration due to gravity (m/s^2). Default is 9.81 m/s^2 (standard gravity)
        thrower_height : Optional, float
            Height of the thrower (m). Default is 1.83 m
        throwing_speed : Optional, float
            Speed at which the ball is thrown (m/s). Default is 40 m/s
    """

    inputs = []  # no inputs, no way to control
    states = [
        'x',    # Position (m) 
        'v',    # Velocity (m/s)
        'max_x' # Maximum state
        ]
    outputs = [
        'x'     # Position (m)
    ]
    events = [
        'falling',  # Event- object is falling
        'impact'    # Event- object has impacted ground
    ]

    is_vectorized = True

    # The Default parameters. Overwritten by passing parameters dictionary into constructor
    default_parameters = {
        'thrower_height': 1.83,  # m
        'throwing_speed': 40,  # m/s
        'g': -9.81,  # Acceleration due to gravity in m/s^2
        'process_noise': 0.0  # amount of noise in each step
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_x = 0.0

    def initialize(self, u=None, z=None):
        return {
            'x': self.parameters['thrower_height'],  # Thrown, so initial altitude is height of thrower
            'v': self.parameters['throwing_speed'],  # Velocity at which the ball is thrown - this guy is a professional baseball pitcher
            'max_x': self.parameters['thrower_height']
            }
    
    def next_state(self, x, u, dt):
        next_x =  x['x'] + x['v']*dt
        return {'x': next_x,
                'v': x['v'] + self.parameters['g']*dt,  # Acceleration of gravity
                'max_x': maximum(x['max_x'], next_x)}

    def output(self, x):
        return {'x': x['x']}

    # This is actually optional. Leaving thresholds_met empty will use the event state to define thresholds.
    #  Threshold = Event State == 0. However, this implementation is more efficient, so we included it
    def threshold_met(self, x):
        return {
            'falling': x['v'] < 0,
            'impact': x['x'] <= 0
        }

    def event_state(self, x): 
        x['max_x'] = maximum(x['max_x'], x['x'])  # Maximum altitude
        return {
            'falling': maximum(x['v']/self.parameters['throwing_speed'],0),  # Throwing speed is max speed
            'impact': maximum(x['x']/x['max_x'],0)  # 1 until falling begins, then it's fraction of height
        }
