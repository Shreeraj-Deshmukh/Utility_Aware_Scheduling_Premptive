"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.662532, 'e_o_k': [0.251416, 0.201133, 0.160906, 0.128725, 0.102980, 0.082384], 'p_i': 10, 'u_i': 3.4980},
        {'id': 1, 'e_m': 1.969439, 'e_o_k': [1.531786, 1.225428], 'p_i': 20, 'u_i': 2.1751},
        {'id': 2, 'e_m': 0.768607, 'e_o_k': [0.320101, 0.256080, 0.204864, 0.163891, 0.131113], 'p_i': 40, 'u_i': 4.1688},
        {'id': 3, 'e_m': 2.851730, 'e_o_k': [1.636238, 1.308991, 1.047193], 'p_i': 80, 'u_i': 2.2140},
        {'id': 4, 'e_m': 0.928463, 'e_o_k': [0.532725, 0.426180, 0.340944], 'p_i': 10, 'u_i': 3.2266},
        {'id': 5, 'e_m': 0.875668, 'e_o_k': [0.332296, 0.265837, 0.212670, 0.170136, 0.136109, 0.108887], 'p_i': 10, 'u_i': 3.3398},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
