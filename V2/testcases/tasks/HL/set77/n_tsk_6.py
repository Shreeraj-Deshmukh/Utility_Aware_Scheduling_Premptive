"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.608308, 'e_o_k': [0.124653, 0.099723, 0.079778], 'p_i': 10, 'u_i': 2.5184},
        {'id': 1, 'e_m': 4.670017, 'e_o_k': [0.694612, 0.555690, 0.444552, 0.355641, 0.284513], 'p_i': 20, 'u_i': 4.2996},
        {'id': 2, 'e_m': 6.040063, 'e_o_k': [0.818596, 0.654877, 0.523902, 0.419121, 0.335297, 0.268238], 'p_i': 40, 'u_i': 3.3901},
        {'id': 3, 'e_m': 1.905406, 'e_o_k': [0.258236, 0.206588, 0.165271, 0.132217, 0.105773, 0.084619], 'p_i': 80, 'u_i': 2.3217},
        {'id': 4, 'e_m': 20.651648, 'e_o_k': [3.497908, 2.798326, 2.238661, 1.790929], 'p_i': 80, 'u_i': 2.1118},
        {'id': 5, 'e_m': 5.816289, 'e_o_k': [0.985144, 0.788115, 0.630492, 0.504394], 'p_i': 80, 'u_i': 4.2305},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
