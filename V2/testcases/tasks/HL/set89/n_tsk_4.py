"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.570637, 'e_o_k': [0.382353, 0.305883, 0.244706, 0.195765, 0.156612], 'p_i': 10, 'u_i': 2.3680},
        {'id': 1, 'e_m': 3.479846, 'e_o_k': [0.966624, 0.773299], 'p_i': 20, 'u_i': 4.2120},
        {'id': 2, 'e_m': 5.793520, 'e_o_k': [1.609311, 1.287449], 'p_i': 40, 'u_i': 4.4653},
        {'id': 3, 'e_m': 17.928476, 'e_o_k': [4.980132, 3.984106], 'p_i': 80, 'u_i': 4.6069},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
