"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.143220, 'e_o_k': [0.234266, 0.187413, 0.149931], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 0.721620, 'e_o_k': [0.147873, 0.118298, 0.094639], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 0.561215, 'e_o_k': [0.115003, 0.092002, 0.073602], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 9.907138, 'e_o_k': [2.030151, 1.624121, 1.299297], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 0.924900, 'e_o_k': [0.189529, 0.151623, 0.121298], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 1.311382, 'e_o_k': [0.268726, 0.214981, 0.171985], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.152759, 'e_o_k': [0.031303, 0.025042, 0.020034], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 1.231826, 'e_o_k': [0.252423, 0.201939, 0.161551], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
