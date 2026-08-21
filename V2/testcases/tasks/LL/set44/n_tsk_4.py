"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.289987, 'e_o_k': [0.043132, 0.034506, 0.027605, 0.022084, 0.017667], 'p_i': 10, 'u_i': 4.1808},
        {'id': 1, 'e_m': 2.987330, 'e_o_k': [0.404866, 0.323893, 0.259114, 0.207292, 0.165833, 0.132667], 'p_i': 20, 'u_i': 4.1927},
        {'id': 2, 'e_m': 2.188429, 'e_o_k': [0.448449, 0.358759, 0.287007], 'p_i': 40, 'u_i': 3.7566},
        {'id': 3, 'e_m': 13.353922, 'e_o_k': [2.736459, 2.189168, 1.751334], 'p_i': 80, 'u_i': 3.2050},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
