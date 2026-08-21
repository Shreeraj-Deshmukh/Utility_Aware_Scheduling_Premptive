"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.987927, 'e_o_k': [0.146943, 0.117554, 0.094043, 0.075235, 0.060188], 'p_i': 10, 'u_i': 1.8790},
        {'id': 1, 'e_m': 7.460876, 'e_o_k': [1.109721, 0.887777, 0.710221, 0.568177, 0.454542], 'p_i': 20, 'u_i': 3.3534},
        {'id': 2, 'e_m': 8.597414, 'e_o_k': [1.761765, 1.409412, 1.127530], 'p_i': 40, 'u_i': 2.5184},
        {'id': 3, 'e_m': 9.058254, 'e_o_k': [1.347313, 1.077850, 0.862280, 0.689824, 0.551859], 'p_i': 80, 'u_i': 4.2996},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
