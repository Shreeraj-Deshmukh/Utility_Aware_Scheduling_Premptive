"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.735977, 'e_o_k': [0.109468, 0.087575, 0.070060, 0.056048, 0.044838], 'p_i': 10, 'u_i': 1.2401},
        {'id': 1, 'e_m': 1.272862, 'e_o_k': [0.189324, 0.151459, 0.121167, 0.096934, 0.077547], 'p_i': 20, 'u_i': 2.2762},
        {'id': 2, 'e_m': 6.649816, 'e_o_k': [0.989085, 0.791268, 0.633014, 0.506411, 0.405129], 'p_i': 40, 'u_i': 1.0661},
        {'id': 3, 'e_m': 7.721105, 'e_o_k': [1.307775, 1.046220, 0.836976, 0.669581], 'p_i': 80, 'u_i': 2.9903},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
