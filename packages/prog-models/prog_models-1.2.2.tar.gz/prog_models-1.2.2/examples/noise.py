# Copyright © 2021 United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration.  All Rights Reserved.

"""
Example defining and testing a new model. 
"""

# Deriv prog model was selected because the model can be described as x' = x + dx*dt
from prog_models.models.thrown_object import ThrownObject

def run_example():
    def future_load(t, x=None):
        return {}
    event = 'impact'

    # Ex1: No noise
    process_noise = 0
    m = ThrownObject(process_noise = process_noise)
    (times, _, states, outputs, _) = m.simulate_to_threshold(future_load, threshold_keys=[event], dt=0.005, save_freq=1)
    print('Example without noise')
    print('\t- states: {}'.format(['{}s: {}'.format(round(t,2), x) for (t,x) in zip(times, states)])) 
    print('\t- impact time: {}s'.format(times[-1]))

    # Ex2: with noise - same noise applied to every state
    process_noise = 0.5
    m = ThrownObject(process_noise = process_noise)  # Noise with a std of 0.5 to every state
    print('\nExample without same noise for every state')
    (times, _, states, outputs, _) = m.simulate_to_threshold(future_load, threshold_keys=[event], dt=0.005, save_freq=1)
    print('\t- states: {}'.format(['{}s: {}'.format(round(t,2), x) for (t,x) in zip(times, states)])) 
    print('\t- impact time: {}s'.format(times[-1]))

    # Ex3: noise- more noise on position than velocity
    process_noise = {'x': 0.25, 'v': 0.75, 'max_x': 0}
    m = ThrownObject(process_noise = process_noise) 
    print('\nExample with more noise on position than velocity')
    (times, _, states, outputs, _) = m.simulate_to_threshold(future_load, threshold_keys=[event], dt=0.005, save_freq=1)
    print('\t- states: {}'.format(['{}s: {}'.format(round(t,2), x) for (t,x) in zip(times, states)])) 
    print('\t- impact time: {}s'.format(times[-1]))

    # Ex4: noise- Ex3 but uniform
    process_noise = {'x': 0.25, 'v': 0.75, 'max_x': 0}
    process_noise_dist = 'uniform'
    model_config = {'process_noise_dist': process_noise_dist, 'process_noise': process_noise}
    m = ThrownObject(**model_config) 
    print('\nExample with more uniform noise')
    (times, _, states, outputs, _) = m.simulate_to_threshold(future_load, threshold_keys=[event], dt=0.005, save_freq=1)
    print('\t- states: {}'.format(['{}s: {}'.format(round(t,2), x) for (t,x) in zip(times, states)])) 
    print('\t- impact time: {}s'.format(times[-1]))

    # Ex5: noise- Ex3 but triangle
    process_noise = {'x': 0.25, 'v': 0.75, 'max_x': 1e-9}
    process_noise_dist = 'triangular'
    model_config = {'process_noise_dist': process_noise_dist, 'process_noise': process_noise}
    m = ThrownObject(**model_config) 
    print('\nExample with triangular process noise')
    (times, _, states, outputs, _) = m.simulate_to_threshold(future_load, threshold_keys=[event], dt=0.005, save_freq=1)
    print('\t- states: {}'.format(['{}s: {}'.format(round(t,2), x) for (t,x) in zip(times, states)])) 
    print('\t- impact time: {}s'.format(times[-1]))

    # Ex6: Measurement noise
    # Everything we've done with process noise, we can also do with measurement noise.
    # Just use 'measurement_noise' and 'measurement_noise_dist' 
    measurement_noise = {'x': 0.25}  # For each output
    measurement_noise_dist = 'uniform'
    model_config = {'measurement_noise_dist': measurement_noise_dist, 'measurement_noise': measurement_noise}
    m = ThrownObject(**model_config) 
    print('\nExample with measurement noise')
    (times, _, states, outputs, _) = m.simulate_to_threshold(future_load, threshold_keys=[event], dt=0.005, save_freq=1)
    print('\t- states: {}'.format(['{}s: {}'.format(round(t,2), x) for (t,x) in zip(times, states)])) 
    print('\t- outputs: {}'.format(['{}s: {}'.format(round(t,2), x) for (t,x) in zip(times, outputs)])) 
    print('\t- impact time: {}s'.format(times[-1]))
    print(' note the output is sometimes not the same as state- that is the measurement noise')

    # Ex7: OK, now for something a little more complicated. Let's try proportional noise on v only (more variation when it's going faster)
    # This can be used to do custom or more complex noise distributions
    def apply_proportional_process_noise(self, x, dt = 1):
        return {
            'x': x['x'],  # No noise on state
            'v': x['v'] - dt*0.5*x['v'],
            'max_x': x['max_x']  # No noise on max_x
        }
    model_config = {'process_noise': apply_proportional_process_noise}
    m = ThrownObject(**model_config)
    print('\nExample with proportional noise on velocity')
    (times, _, states, outputs, _) = m.simulate_to_threshold(future_load, threshold_keys=[event], dt=0.005, save_freq=1)
    print('\t- states: {}'.format(['{}s: {}'.format(round(t,2), x) for (t,x) in zip(times, states)])) 
    print('\t- impact time: {}s'.format(times[-1]))

# This allows the module to be executed directly 
if __name__=='__main__':
    run_example()
