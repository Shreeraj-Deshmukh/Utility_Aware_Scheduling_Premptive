"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.160373, 'e_o_k': [0.023854, 0.019083, 0.015266, 0.012213, 0.009770], 'p_i': 10, 'u_i': 1.6464},
        {'id': 1, 'e_m': 1.239537, 'e_o_k': [0.344316, 0.275453], 'p_i': 20, 'u_i': 4.4830},
        {'id': 2, 'e_m': 3.471757, 'e_o_k': [0.470520, 0.376416, 0.301133, 0.240906, 0.192725, 0.154180], 'p_i': 40, 'u_i': 3.9048},
        {'id': 3, 'e_m': 4.241467, 'e_o_k': [0.630870, 0.504696, 0.403757, 0.323006, 0.258404], 'p_i': 80, 'u_i': 3.4604},
        {'id': 4, 'e_m': 2.172428, 'e_o_k': [0.445170, 0.356136, 0.284909], 'p_i': 20, 'u_i': 2.2645},
        {'id': 5, 'e_m': 0.735522, 'e_o_k': [0.109401, 0.087520, 0.070016, 0.056013, 0.044810], 'p_i': 10, 'u_i': 4.9290},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
