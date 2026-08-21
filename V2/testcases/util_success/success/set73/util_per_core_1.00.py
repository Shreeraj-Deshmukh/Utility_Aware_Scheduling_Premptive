"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.166806, 'e_o_k': [0.423456, 0.338765, 0.271012, 0.216809], 'p_i': 10, 'u_i': 2.5191},
        {'id': 1, 'e_m': 1.450864, 'e_o_k': [0.117979, 0.094384, 0.075507, 0.060405, 0.048324, 0.038659], 'p_i': 20, 'u_i': 1.4276},
        {'id': 2, 'e_m': 4.575414, 'e_o_k': [0.408325, 0.326660, 0.261328, 0.209062, 0.167250], 'p_i': 40, 'u_i': 2.4044},
        {'id': 3, 'e_m': 12.943989, 'e_o_k': [1.315446, 1.052357, 0.841885, 0.673508], 'p_i': 80, 'u_i': 3.6414},
        {'id': 4, 'e_m': 3.858574, 'e_o_k': [0.344352, 0.275481, 0.220385, 0.176308, 0.141046], 'p_i': 20, 'u_i': 3.1817},
        {'id': 5, 'e_m': 3.548423, 'e_o_k': [0.591404, 0.473123], 'p_i': 10, 'u_i': 1.8252},
        {'id': 6, 'e_m': 11.490719, 'e_o_k': [1.412793, 1.130235, 0.904188], 'p_i': 40, 'u_i': 3.6022},
        {'id': 7, 'e_m': 31.964164, 'e_o_k': [5.327361, 4.261889], 'p_i': 80, 'u_i': 2.1719},
    ]
    B_BUDGET = 239.200003
    return processors, tasks, B_BUDGET
