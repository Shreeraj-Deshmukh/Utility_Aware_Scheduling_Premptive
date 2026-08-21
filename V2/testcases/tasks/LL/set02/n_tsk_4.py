"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.781465, 'e_o_k': [0.160136, 0.128109, 0.102487], 'p_i': 10, 'u_i': 2.1098},
        {'id': 1, 'e_m': 2.259168, 'e_o_k': [0.462944, 0.370355, 0.296284], 'p_i': 20, 'u_i': 3.5044},
        {'id': 2, 'e_m': 6.509630, 'e_o_k': [0.882236, 0.705789, 0.564631, 0.451705, 0.361364, 0.289091], 'p_i': 40, 'u_i': 1.3726},
        {'id': 3, 'e_m': 3.692349, 'e_o_k': [0.549195, 0.439356, 0.351485, 0.281188, 0.224950], 'p_i': 80, 'u_i': 3.0405},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
