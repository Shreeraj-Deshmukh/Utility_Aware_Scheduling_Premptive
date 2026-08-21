"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760003, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760003, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.500725, 'e_o_k': [0.050887, 0.040709, 0.032567, 0.026054], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 0.767104, 'e_o_k': [0.077958, 0.062366, 0.049893, 0.039914], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 3.714493, 'e_o_k': [0.619082, 0.495266], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 5.645701, 'e_o_k': [0.694144, 0.555315, 0.444252], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.394442, 'e_o_k': [0.048497, 0.038798, 0.031038], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 11.776094, 'e_o_k': [1.962682, 1.570146], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 4.652722, 'e_o_k': [0.775454, 0.620363], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 5.980679, 'e_o_k': [0.996780, 0.797424], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 71.760003
    return processors, tasks, B_BUDGET
