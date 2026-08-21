"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.492663, 'e_o_k': [1.247962, 0.998370], 'p_i': 10, 'u_i': 1.0738},
        {'id': 1, 'e_m': 1.261030, 'e_o_k': [0.213589, 0.170871, 0.136697, 0.109358], 'p_i': 20, 'u_i': 3.3187},
        {'id': 2, 'e_m': 3.885238, 'e_o_k': [0.796155, 0.636924, 0.509539], 'p_i': 40, 'u_i': 4.5515},
        {'id': 3, 'e_m': 15.244097, 'e_o_k': [4.234471, 3.387577], 'p_i': 80, 'u_i': 3.0521},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
