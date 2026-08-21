"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.251346, 'e_o_k': [0.037385, 0.029908, 0.023926, 0.019141, 0.015313], 'p_i': 10, 'u_i': 1.3020},
        {'id': 1, 'e_m': 1.536630, 'e_o_k': [0.228556, 0.182845, 0.146276, 0.117021, 0.093617], 'p_i': 20, 'u_i': 4.0316},
        {'id': 2, 'e_m': 10.919463, 'e_o_k': [2.237595, 1.790076, 1.432061], 'p_i': 40, 'u_i': 1.7419},
        {'id': 3, 'e_m': 2.003788, 'e_o_k': [0.339395, 0.271516, 0.217213, 0.173770], 'p_i': 80, 'u_i': 1.0689},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
