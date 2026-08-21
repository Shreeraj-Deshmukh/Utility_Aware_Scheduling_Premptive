"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.467876, 'e_o_k': [0.177549, 0.142039, 0.113631, 0.090905, 0.072724, 0.058179], 'p_i': 10, 'u_i': 2.7067},
        {'id': 1, 'e_m': 1.187129, 'e_o_k': [0.450489, 0.360391, 0.288313, 0.230651, 0.184520, 0.147616], 'p_i': 20, 'u_i': 4.2680},
        {'id': 2, 'e_m': 0.390401, 'e_o_k': [0.162590, 0.130072, 0.104057, 0.083246, 0.066597], 'p_i': 40, 'u_i': 4.9110},
        {'id': 3, 'e_m': 13.315458, 'e_o_k': [5.052921, 4.042337, 3.233870, 2.587096, 2.069676, 1.655741], 'p_i': 80, 'u_i': 1.5555},
        {'id': 4, 'e_m': 0.925085, 'e_o_k': [0.530786, 0.424629, 0.339703], 'p_i': 20, 'u_i': 1.9189},
        {'id': 5, 'e_m': 5.711876, 'e_o_k': [4.442570, 3.554056], 'p_i': 80, 'u_i': 3.1608},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
