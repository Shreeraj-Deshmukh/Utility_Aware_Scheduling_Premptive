"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.212365, 'e_o_k': [0.942950, 0.754360], 'p_i': 10, 'u_i': 2.3775},
        {'id': 1, 'e_m': 3.453615, 'e_o_k': [1.438322, 1.150657, 0.920526, 0.736421, 0.589136], 'p_i': 20, 'u_i': 3.1328},
        {'id': 2, 'e_m': 3.359717, 'e_o_k': [1.927707, 1.542165, 1.233732], 'p_i': 40, 'u_i': 3.5798},
        {'id': 3, 'e_m': 1.767187, 'e_o_k': [0.735977, 0.588782, 0.471026, 0.376820, 0.301456], 'p_i': 80, 'u_i': 2.6618},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
