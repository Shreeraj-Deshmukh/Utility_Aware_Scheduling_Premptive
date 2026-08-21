"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640011, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640011, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.793526, 'e_o_k': [0.617187, 0.493749], 'p_i': 10, 'u_i': 3.3143},
        {'id': 1, 'e_m': 1.049928, 'e_o_k': [0.816611, 0.653289], 'p_i': 20, 'u_i': 3.2246},
        {'id': 2, 'e_m': 7.537585, 'e_o_k': [5.862566, 4.690053], 'p_i': 40, 'u_i': 4.6504},
        {'id': 3, 'e_m': 17.122126, 'e_o_k': [13.317209, 10.653767], 'p_i': 80, 'u_i': 4.9346},
        {'id': 4, 'e_m': 0.854071, 'e_o_k': [0.664278, 0.531422], 'p_i': 10, 'u_i': 2.0105},
        {'id': 5, 'e_m': 3.312634, 'e_o_k': [2.576493, 2.061194], 'p_i': 40, 'u_i': 3.0068},
        {'id': 6, 'e_m': 1.838787, 'e_o_k': [1.430168, 1.144134], 'p_i': 80, 'u_i': 1.6248},
        {'id': 7, 'e_m': 5.958164, 'e_o_k': [4.634127, 3.707302], 'p_i': 80, 'u_i': 2.1190},
    ]
    B_BUDGET = 176.640011
    return processors, tasks, B_BUDGET
