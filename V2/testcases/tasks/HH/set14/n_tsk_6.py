"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.992831, 'e_o_k': [0.376757, 0.301406, 0.241125, 0.192900, 0.154320, 0.123456], 'p_i': 10, 'u_i': 2.9591},
        {'id': 1, 'e_m': 4.212824, 'e_o_k': [1.754508, 1.403606, 1.122885, 0.898308, 0.718646], 'p_i': 20, 'u_i': 3.3490},
        {'id': 2, 'e_m': 13.197470, 'e_o_k': [10.264699, 8.211759], 'p_i': 40, 'u_i': 1.0216},
        {'id': 3, 'e_m': 4.415523, 'e_o_k': [2.533497, 2.026798, 1.621438], 'p_i': 80, 'u_i': 4.0085},
        {'id': 4, 'e_m': 0.055512, 'e_o_k': [0.031851, 0.025481, 0.020385], 'p_i': 20, 'u_i': 1.9931},
        {'id': 5, 'e_m': 8.173545, 'e_o_k': [4.689739, 3.751791, 3.001433], 'p_i': 80, 'u_i': 2.4773},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
