"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.571521, 'e_o_k': [0.077457, 0.061966, 0.049573, 0.039658, 0.031726, 0.025381], 'p_i': 10, 'u_i': 2.5404},
        {'id': 1, 'e_m': 1.425904, 'e_o_k': [0.292193, 0.233755, 0.187004], 'p_i': 20, 'u_i': 1.0986},
        {'id': 2, 'e_m': 1.552851, 'e_o_k': [0.431347, 0.345078], 'p_i': 40, 'u_i': 3.7025},
        {'id': 3, 'e_m': 9.264581, 'e_o_k': [2.573495, 2.058796], 'p_i': 80, 'u_i': 4.4926},
        {'id': 4, 'e_m': 0.961546, 'e_o_k': [0.197038, 0.157631, 0.126104], 'p_i': 80, 'u_i': 3.2922},
        {'id': 5, 'e_m': 4.196193, 'e_o_k': [1.165609, 0.932487], 'p_i': 40, 'u_i': 3.7450},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
