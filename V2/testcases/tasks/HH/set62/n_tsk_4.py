"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.097419, 'e_o_k': [3.186882, 2.549505], 'p_i': 10, 'u_i': 3.2108},
        {'id': 1, 'e_m': 3.168359, 'e_o_k': [2.464279, 1.971423], 'p_i': 20, 'u_i': 1.2189},
        {'id': 2, 'e_m': 2.648778, 'e_o_k': [1.005153, 0.804122, 0.643298, 0.514638, 0.411710, 0.329368], 'p_i': 40, 'u_i': 1.4602},
        {'id': 3, 'e_m': 13.249655, 'e_o_k': [10.305287, 8.244230], 'p_i': 80, 'u_i': 2.5890},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
