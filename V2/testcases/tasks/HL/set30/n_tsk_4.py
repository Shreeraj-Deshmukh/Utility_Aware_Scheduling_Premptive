"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.113918, 'e_o_k': [0.023344, 0.018675, 0.014940], 'p_i': 10, 'u_i': 4.7642},
        {'id': 1, 'e_m': 5.480782, 'e_o_k': [0.815204, 0.652163, 0.521731, 0.417385, 0.333908], 'p_i': 20, 'u_i': 4.7668},
        {'id': 2, 'e_m': 8.277898, 'e_o_k': [1.121885, 0.897508, 0.718007, 0.574405, 0.459524, 0.367619], 'p_i': 40, 'u_i': 4.7724},
        {'id': 3, 'e_m': 24.609731, 'e_o_k': [3.660419, 2.928335, 2.342668, 1.874135, 1.499308], 'p_i': 80, 'u_i': 4.0150},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
