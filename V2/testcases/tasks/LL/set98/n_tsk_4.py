"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.756013, 'e_o_k': [0.237989, 0.190391, 0.152313, 0.121850, 0.097480, 0.077984], 'p_i': 10, 'u_i': 4.8035},
        {'id': 1, 'e_m': 1.219078, 'e_o_k': [0.181324, 0.145059, 0.116047, 0.092838, 0.074270], 'p_i': 20, 'u_i': 1.9119},
        {'id': 2, 'e_m': 4.552641, 'e_o_k': [1.264622, 1.011698], 'p_i': 40, 'u_i': 3.5492},
        {'id': 3, 'e_m': 3.970302, 'e_o_k': [1.102862, 0.882289], 'p_i': 80, 'u_i': 2.1494},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
