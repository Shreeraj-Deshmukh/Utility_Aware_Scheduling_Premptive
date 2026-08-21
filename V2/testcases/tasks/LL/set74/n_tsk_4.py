"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.271924, 'e_o_k': [0.075534, 0.060428], 'p_i': 10, 'u_i': 4.4654},
        {'id': 1, 'e_m': 2.850575, 'e_o_k': [0.584134, 0.467307, 0.373846], 'p_i': 20, 'u_i': 1.2910},
        {'id': 2, 'e_m': 7.504114, 'e_o_k': [1.017016, 0.813613, 0.650890, 0.520712, 0.416570, 0.333256], 'p_i': 40, 'u_i': 1.4207},
        {'id': 3, 'e_m': 3.414082, 'e_o_k': [0.507806, 0.406245, 0.324996, 0.259997, 0.207997], 'p_i': 80, 'u_i': 4.1417},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
