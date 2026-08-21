"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.190184, 'e_o_k': [0.161303, 0.129042, 0.103234, 0.082587, 0.066070, 0.052856], 'p_i': 10, 'u_i': 2.2901},
        {'id': 1, 'e_m': 2.932524, 'e_o_k': [0.814590, 0.651672], 'p_i': 20, 'u_i': 4.0645},
        {'id': 2, 'e_m': 5.307615, 'e_o_k': [0.719329, 0.575463, 0.460371, 0.368297, 0.294637, 0.235710], 'p_i': 40, 'u_i': 4.5754},
        {'id': 3, 'e_m': 0.133200, 'e_o_k': [0.022561, 0.018049, 0.014439, 0.011551], 'p_i': 80, 'u_i': 3.5388},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET
