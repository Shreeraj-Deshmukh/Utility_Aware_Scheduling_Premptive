"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.246332, 'e_o_k': [0.623981, 0.499185], 'p_i': 10, 'u_i': 1.0738},
        {'id': 1, 'e_m': 0.630515, 'e_o_k': [0.106795, 0.085436, 0.068349, 0.054679], 'p_i': 20, 'u_i': 3.3187},
        {'id': 2, 'e_m': 1.942619, 'e_o_k': [0.398078, 0.318462, 0.254770], 'p_i': 40, 'u_i': 4.5515},
        {'id': 3, 'e_m': 7.622048, 'e_o_k': [2.117236, 1.693789], 'p_i': 80, 'u_i': 3.0521},
    ]
    B_BUDGET = 55.200013
    return processors, tasks, B_BUDGET
