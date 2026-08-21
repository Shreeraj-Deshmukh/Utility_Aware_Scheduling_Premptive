"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.232334, 'e_o_k': [0.457446, 0.365956, 0.292765], 'p_i': 10, 'u_i': 2.7485},
        {'id': 1, 'e_m': 1.449433, 'e_o_k': [0.215587, 0.172469, 0.137976, 0.110380, 0.088304], 'p_i': 20, 'u_i': 3.8876},
        {'id': 2, 'e_m': 1.798956, 'e_o_k': [0.267574, 0.214059, 0.171248, 0.136998, 0.109598], 'p_i': 40, 'u_i': 1.4132},
        {'id': 3, 'e_m': 4.745682, 'e_o_k': [0.803808, 0.643046, 0.514437, 0.411550], 'p_i': 80, 'u_i': 3.6535},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
