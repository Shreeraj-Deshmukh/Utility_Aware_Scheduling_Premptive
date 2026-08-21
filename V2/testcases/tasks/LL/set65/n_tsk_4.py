"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.147524, 'e_o_k': [0.024987, 0.019990, 0.015992, 0.012793], 'p_i': 10, 'u_i': 4.6168},
        {'id': 1, 'e_m': 5.000513, 'e_o_k': [0.677708, 0.542167, 0.433733, 0.346987, 0.277589, 0.222072], 'p_i': 20, 'u_i': 1.2568},
        {'id': 2, 'e_m': 0.907188, 'e_o_k': [0.134934, 0.107947, 0.086358, 0.069086, 0.055269], 'p_i': 40, 'u_i': 3.3453},
        {'id': 3, 'e_m': 9.003385, 'e_o_k': [1.844956, 1.475965, 1.180772], 'p_i': 80, 'u_i': 2.8841},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
