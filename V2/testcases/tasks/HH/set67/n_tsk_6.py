"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.560347, 'e_o_k': [2.162766, 1.730213, 1.384170, 1.107336], 'p_i': 10, 'u_i': 1.8147},
        {'id': 1, 'e_m': 0.119200, 'e_o_k': [0.056531, 0.045225, 0.036180, 0.028944], 'p_i': 20, 'u_i': 2.7697},
        {'id': 2, 'e_m': 5.951871, 'e_o_k': [2.258603, 1.806882, 1.445506, 1.156405, 0.925124, 0.740099], 'p_i': 40, 'u_i': 2.4720},
        {'id': 3, 'e_m': 2.781198, 'e_o_k': [2.163154, 1.730523], 'p_i': 80, 'u_i': 3.3220},
        {'id': 4, 'e_m': 8.400858, 'e_o_k': [6.534000, 5.227200], 'p_i': 80, 'u_i': 2.5309},
        {'id': 5, 'e_m': 0.988657, 'e_o_k': [0.567262, 0.453810, 0.363048], 'p_i': 20, 'u_i': 3.7128},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
