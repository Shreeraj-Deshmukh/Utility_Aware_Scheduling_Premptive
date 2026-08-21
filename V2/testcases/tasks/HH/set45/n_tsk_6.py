"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.132920, 'e_o_k': [0.055357, 0.044285, 0.035428, 0.028343, 0.022674], 'p_i': 10, 'u_i': 4.9998},
        {'id': 1, 'e_m': 1.465834, 'e_o_k': [1.140093, 0.912074], 'p_i': 20, 'u_i': 2.8601},
        {'id': 2, 'e_m': 0.036091, 'e_o_k': [0.017116, 0.013693, 0.010954, 0.008763], 'p_i': 40, 'u_i': 4.7969},
        {'id': 3, 'e_m': 4.215245, 'e_o_k': [1.755516, 1.404413, 1.123530, 0.898824, 0.719059], 'p_i': 80, 'u_i': 4.3760},
        {'id': 4, 'e_m': 15.724840, 'e_o_k': [9.022449, 7.217959, 5.774367], 'p_i': 80, 'u_i': 3.1042},
        {'id': 5, 'e_m': 37.061042, 'e_o_k': [14.063844, 11.251075, 9.000860, 7.200688, 5.760551, 4.608440], 'p_i': 80, 'u_i': 1.7042},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
