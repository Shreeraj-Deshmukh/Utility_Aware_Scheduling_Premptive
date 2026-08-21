"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600008, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600008, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.549233, 'e_o_k': [0.044662, 0.035729, 0.028584, 0.022867, 0.018293, 0.014635], 'p_i': 10, 'u_i': 3.3901},
        {'id': 1, 'e_m': 4.226526, 'e_o_k': [0.343687, 0.274950, 0.219960, 0.175968, 0.140774, 0.112619], 'p_i': 20, 'u_i': 2.3217},
        {'id': 2, 'e_m': 5.626384, 'e_o_k': [0.571787, 0.457430, 0.365944, 0.292755], 'p_i': 40, 'u_i': 2.1118},
        {'id': 3, 'e_m': 1.620841, 'e_o_k': [0.164720, 0.131776, 0.105421, 0.084336], 'p_i': 80, 'u_i': 4.2305},
        {'id': 4, 'e_m': 18.172425, 'e_o_k': [3.028738, 2.422990], 'p_i': 80, 'u_i': 2.0791},
        {'id': 5, 'e_m': 9.935270, 'e_o_k': [1.655878, 1.324703], 'p_i': 80, 'u_i': 1.4810},
        {'id': 6, 'e_m': 9.045148, 'e_o_k': [1.507525, 1.206020], 'p_i': 80, 'u_i': 3.5439},
        {'id': 7, 'e_m': 1.084197, 'e_o_k': [0.088163, 0.070531, 0.056425, 0.045140, 0.036112, 0.028889], 'p_i': 10, 'u_i': 4.1958},
    ]
    B_BUDGET = 119.600008
    return processors, tasks, B_BUDGET
