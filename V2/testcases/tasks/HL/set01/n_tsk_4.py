"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.617360, 'e_o_k': [0.091825, 0.073460, 0.058768, 0.047015, 0.037612], 'p_i': 10, 'u_i': 4.1247},
        {'id': 1, 'e_m': 5.349248, 'e_o_k': [1.096157, 0.876926, 0.701541], 'p_i': 20, 'u_i': 3.4312},
        {'id': 2, 'e_m': 11.779971, 'e_o_k': [3.272214, 2.617771], 'p_i': 40, 'u_i': 1.1226},
        {'id': 3, 'e_m': 14.104185, 'e_o_k': [2.097838, 1.678270, 1.342616, 1.074093, 0.859274], 'p_i': 80, 'u_i': 3.8598},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
