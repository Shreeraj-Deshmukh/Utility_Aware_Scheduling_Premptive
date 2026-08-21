"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.512026, 'e_o_k': [0.475977, 0.380782, 0.304625, 0.243700, 0.194960, 0.155968], 'p_i': 10, 'u_i': 4.8035},
        {'id': 1, 'e_m': 2.438156, 'e_o_k': [0.362648, 0.290118, 0.232095, 0.185676, 0.148541], 'p_i': 20, 'u_i': 1.9119},
        {'id': 2, 'e_m': 9.105282, 'e_o_k': [2.529245, 2.023396], 'p_i': 40, 'u_i': 3.5492},
        {'id': 3, 'e_m': 7.940603, 'e_o_k': [2.205723, 1.764579], 'p_i': 80, 'u_i': 2.1494},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
