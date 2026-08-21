"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.600854, 'e_o_k': [0.081432, 0.065146, 0.052117, 0.041693, 0.033355, 0.026684], 'p_i': 10, 'u_i': 4.4924},
        {'id': 1, 'e_m': 1.220515, 'e_o_k': [0.250105, 0.200084, 0.160068], 'p_i': 20, 'u_i': 4.2054},
        {'id': 2, 'e_m': 8.826737, 'e_o_k': [1.312877, 1.050302, 0.840241, 0.672193, 0.537755], 'p_i': 40, 'u_i': 2.8306},
        {'id': 3, 'e_m': 0.565020, 'e_o_k': [0.156950, 0.125560], 'p_i': 80, 'u_i': 2.8504},
        {'id': 4, 'e_m': 0.405741, 'e_o_k': [0.054989, 0.043991, 0.035193, 0.028154, 0.022524, 0.018019], 'p_i': 10, 'u_i': 1.4385},
        {'id': 5, 'e_m': 0.846685, 'e_o_k': [0.114749, 0.091800, 0.073440, 0.058752, 0.047001, 0.037601], 'p_i': 80, 'u_i': 4.3024},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
