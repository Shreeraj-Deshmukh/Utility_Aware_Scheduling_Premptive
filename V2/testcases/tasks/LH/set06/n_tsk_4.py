"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.190184, 'e_o_k': [0.451649, 0.361319, 0.289055, 0.231244, 0.184995, 0.147996], 'p_i': 10, 'u_i': 2.2901},
        {'id': 1, 'e_m': 2.932524, 'e_o_k': [2.280852, 1.824682], 'p_i': 20, 'u_i': 4.0645},
        {'id': 2, 'e_m': 5.307615, 'e_o_k': [2.014122, 1.611298, 1.289038, 1.031231, 0.824984, 0.659988], 'p_i': 40, 'u_i': 4.5754},
        {'id': 3, 'e_m': 0.133200, 'e_o_k': [0.063171, 0.050536, 0.040429, 0.032343], 'p_i': 80, 'u_i': 3.5388},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
