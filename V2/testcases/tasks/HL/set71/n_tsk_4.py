"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.145960, 'e_o_k': [1.151656, 0.921324], 'p_i': 10, 'u_i': 3.4158},
        {'id': 1, 'e_m': 0.792926, 'e_o_k': [0.220257, 0.176206], 'p_i': 20, 'u_i': 2.7668},
        {'id': 2, 'e_m': 2.834056, 'e_o_k': [0.580749, 0.464599, 0.371679], 'p_i': 40, 'u_i': 2.4237},
        {'id': 3, 'e_m': 21.992501, 'e_o_k': [2.980595, 2.384476, 1.907581, 1.526065, 1.220852, 0.976681], 'p_i': 80, 'u_i': 3.6832},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET
