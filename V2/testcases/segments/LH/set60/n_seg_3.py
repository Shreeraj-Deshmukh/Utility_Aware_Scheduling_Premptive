"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.728311, 'e_o_k': [0.417883, 0.334307, 0.267445], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 3.236491, 'e_o_k': [1.857003, 1.485603, 1.188482], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 0.535015, 'e_o_k': [0.306976, 0.245581, 0.196465], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 4.750488, 'e_o_k': [2.725690, 2.180552, 1.744441], 'p_i': 80, 'u_i': 4.1202},
        {'id': 4, 'e_m': 0.182718, 'e_o_k': [0.104838, 0.083870, 0.067096], 'p_i': 40, 'u_i': 4.7898},
        {'id': 5, 'e_m': 0.092022, 'e_o_k': [0.052800, 0.042240, 0.033792], 'p_i': 10, 'u_i': 3.8151},
        {'id': 6, 'e_m': 2.641333, 'e_o_k': [1.515519, 1.212415, 0.969932], 'p_i': 40, 'u_i': 2.4922},
        {'id': 7, 'e_m': 0.127844, 'e_o_k': [0.073353, 0.058682, 0.046946], 'p_i': 10, 'u_i': 1.4417},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
