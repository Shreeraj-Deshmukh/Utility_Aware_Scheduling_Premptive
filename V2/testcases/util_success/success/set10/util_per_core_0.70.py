"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440003, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440003, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.775641, 'e_o_k': [0.063073, 0.050458, 0.040366, 0.032293, 0.025835, 0.020668], 'p_i': 10, 'u_i': 3.7777},
        {'id': 1, 'e_m': 0.673815, 'e_o_k': [0.060133, 0.048107, 0.038485, 0.030788, 0.024631], 'p_i': 20, 'u_i': 2.9102},
        {'id': 2, 'e_m': 12.577166, 'e_o_k': [1.278167, 1.022534, 0.818027, 0.654422], 'p_i': 40, 'u_i': 3.0744},
        {'id': 3, 'e_m': 36.086246, 'e_o_k': [6.014374, 4.811499], 'p_i': 80, 'u_i': 3.1102},
        {'id': 4, 'e_m': 2.540195, 'e_o_k': [0.206560, 0.165248, 0.132199, 0.105759, 0.084607, 0.067686], 'p_i': 20, 'u_i': 3.9746},
        {'id': 5, 'e_m': 2.356025, 'e_o_k': [0.289675, 0.231740, 0.185392], 'p_i': 10, 'u_i': 1.5757},
        {'id': 6, 'e_m': 3.618890, 'e_o_k': [0.444946, 0.355956, 0.284765], 'p_i': 40, 'u_i': 4.9941},
        {'id': 7, 'e_m': 2.806137, 'e_o_k': [0.467690, 0.374152], 'p_i': 40, 'u_i': 1.7632},
    ]
    B_BUDGET = 167.440003
    return processors, tasks, B_BUDGET
