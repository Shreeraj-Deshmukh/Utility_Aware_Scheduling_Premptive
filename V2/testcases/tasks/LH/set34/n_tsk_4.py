"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320014, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320014, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.251346, 'e_o_k': [0.104678, 0.083742, 0.066994, 0.053595, 0.042876], 'p_i': 10, 'u_i': 1.3020},
        {'id': 1, 'e_m': 1.536630, 'e_o_k': [0.639958, 0.511966, 0.409573, 0.327658, 0.262127], 'p_i': 20, 'u_i': 4.0316},
        {'id': 2, 'e_m': 10.919463, 'e_o_k': [6.265266, 5.012213, 4.009770], 'p_i': 40, 'u_i': 1.7419},
        {'id': 3, 'e_m': 2.003788, 'e_o_k': [0.950306, 0.760245, 0.608196, 0.486557], 'p_i': 80, 'u_i': 1.0689},
    ]
    B_BUDGET = 88.320014
    return processors, tasks, B_BUDGET
