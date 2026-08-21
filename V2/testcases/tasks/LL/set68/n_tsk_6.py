"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.635917, 'e_o_k': [0.107709, 0.086168, 0.068934, 0.055147], 'p_i': 10, 'u_i': 4.9351},
        {'id': 1, 'e_m': 2.189877, 'e_o_k': [0.325719, 0.260576, 0.208460, 0.166768, 0.133415], 'p_i': 20, 'u_i': 4.9277},
        {'id': 2, 'e_m': 1.848218, 'e_o_k': [0.313045, 0.250436, 0.200349, 0.160279], 'p_i': 40, 'u_i': 1.3099},
        {'id': 3, 'e_m': 5.611671, 'e_o_k': [0.950486, 0.760389, 0.608311, 0.486649], 'p_i': 80, 'u_i': 1.1502},
        {'id': 4, 'e_m': 0.302424, 'e_o_k': [0.061972, 0.049578, 0.039662], 'p_i': 10, 'u_i': 2.1747},
        {'id': 5, 'e_m': 1.606415, 'e_o_k': [0.446226, 0.356981], 'p_i': 20, 'u_i': 4.4262},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
