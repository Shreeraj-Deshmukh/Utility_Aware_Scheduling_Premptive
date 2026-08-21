"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640025, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640025, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.920347, 'e_o_k': [1.675609, 1.340487, 1.072390], 'p_i': 10, 'u_i': 1.9752},
        {'id': 1, 'e_m': 0.834414, 'e_o_k': [0.478762, 0.383010, 0.306408], 'p_i': 20, 'u_i': 3.9662},
        {'id': 2, 'e_m': 4.634773, 'e_o_k': [2.659296, 2.127437, 1.701949], 'p_i': 40, 'u_i': 1.9890},
        {'id': 3, 'e_m': 0.634609, 'e_o_k': [0.364120, 0.291296, 0.233037], 'p_i': 80, 'u_i': 3.3639},
        {'id': 4, 'e_m': 3.457185, 'e_o_k': [1.983631, 1.586905, 1.269524], 'p_i': 40, 'u_i': 4.7869},
        {'id': 5, 'e_m': 0.421109, 'e_o_k': [0.241620, 0.193296, 0.154637], 'p_i': 10, 'u_i': 2.7944},
        {'id': 6, 'e_m': 0.414008, 'e_o_k': [0.237546, 0.190036, 0.152029], 'p_i': 10, 'u_i': 4.7769},
        {'id': 7, 'e_m': 1.725014, 'e_o_k': [0.989762, 0.791810, 0.633448], 'p_i': 10, 'u_i': 1.3167},
    ]
    B_BUDGET = 176.640025
    return processors, tasks, B_BUDGET
