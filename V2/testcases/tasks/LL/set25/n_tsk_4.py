"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199988, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199988, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.623021, 'e_o_k': [0.332586, 0.266069, 0.212855], 'p_i': 10, 'u_i': 3.5371},
        {'id': 1, 'e_m': 3.752982, 'e_o_k': [0.769054, 0.615243, 0.492194], 'p_i': 20, 'u_i': 2.5364},
        {'id': 2, 'e_m': 1.311882, 'e_o_k': [0.222202, 0.177762, 0.142209, 0.113768], 'p_i': 40, 'u_i': 2.9162},
        {'id': 3, 'e_m': 1.380136, 'e_o_k': [0.233763, 0.187010, 0.149608, 0.119687], 'p_i': 80, 'u_i': 1.5428},
    ]
    B_BUDGET = 55.199988
    return processors, tasks, B_BUDGET
