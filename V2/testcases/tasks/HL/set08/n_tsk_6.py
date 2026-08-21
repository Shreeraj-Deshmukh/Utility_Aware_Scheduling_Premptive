"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400017, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400017, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.981227, 'e_o_k': [0.132983, 0.106387, 0.085109, 0.068088, 0.054470, 0.043576], 'p_i': 10, 'u_i': 4.9438},
        {'id': 1, 'e_m': 0.148329, 'e_o_k': [0.020103, 0.016082, 0.012866, 0.010293, 0.008234, 0.006587], 'p_i': 20, 'u_i': 2.3791},
        {'id': 2, 'e_m': 8.384770, 'e_o_k': [2.329103, 1.863282], 'p_i': 40, 'u_i': 3.1569},
        {'id': 3, 'e_m': 6.146347, 'e_o_k': [1.041048, 0.832838, 0.666271, 0.533017], 'p_i': 80, 'u_i': 2.0315},
        {'id': 4, 'e_m': 0.305116, 'e_o_k': [0.045383, 0.036306, 0.029045, 0.023236, 0.018589], 'p_i': 10, 'u_i': 1.5871},
        {'id': 5, 'e_m': 7.550015, 'e_o_k': [2.097226, 1.677781], 'p_i': 20, 'u_i': 1.8711},
    ]
    B_BUDGET = 110.400017
    return processors, tasks, B_BUDGET
