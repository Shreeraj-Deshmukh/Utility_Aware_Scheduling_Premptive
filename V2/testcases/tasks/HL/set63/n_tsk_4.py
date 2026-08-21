"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.328551, 'e_o_k': [0.495084, 0.396067, 0.316854, 0.253483, 0.202787], 'p_i': 10, 'u_i': 4.0082},
        {'id': 1, 'e_m': 0.075464, 'e_o_k': [0.010227, 0.008182, 0.006546, 0.005236, 0.004189, 0.003351], 'p_i': 20, 'u_i': 3.2625},
        {'id': 2, 'e_m': 8.498214, 'e_o_k': [1.741437, 1.393150, 1.114520], 'p_i': 40, 'u_i': 3.4071},
        {'id': 3, 'e_m': 20.073309, 'e_o_k': [2.985678, 2.388542, 1.910834, 1.528667, 1.222934], 'p_i': 80, 'u_i': 2.2919},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET
