"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.404009, 'e_o_k': [0.231809, 0.185447, 0.148358], 'p_i': 10, 'u_i': 4.1044},
        {'id': 1, 'e_m': 1.312342, 'e_o_k': [0.752983, 0.602387, 0.481909], 'p_i': 20, 'u_i': 3.5158},
        {'id': 2, 'e_m': 1.516961, 'e_o_k': [0.870387, 0.696310, 0.557048], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 10.070496, 'e_o_k': [5.778153, 4.622523, 3.698018], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 1.082847, 'e_o_k': [0.621305, 0.497044, 0.397636], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.068047, 'e_o_k': [0.039043, 0.031235, 0.024988], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 1.937905, 'e_o_k': [1.111913, 0.889530, 0.711624], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.241844, 'e_o_k': [0.138763, 0.111011, 0.088808], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
