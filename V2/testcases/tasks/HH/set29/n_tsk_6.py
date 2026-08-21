"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.766304, 'e_o_k': [0.319142, 0.255313, 0.204251, 0.163400, 0.130720], 'p_i': 10, 'u_i': 2.3860},
        {'id': 1, 'e_m': 1.223056, 'e_o_k': [0.951266, 0.761013], 'p_i': 20, 'u_i': 2.0962},
        {'id': 2, 'e_m': 5.121185, 'e_o_k': [2.428747, 1.942997, 1.554398, 1.243518], 'p_i': 40, 'u_i': 2.6459},
        {'id': 3, 'e_m': 5.816991, 'e_o_k': [2.207419, 1.765935, 1.412748, 1.130199, 0.904159, 0.723327], 'p_i': 80, 'u_i': 2.9249},
        {'id': 4, 'e_m': 16.250223, 'e_o_k': [6.166599, 4.933279, 3.946624, 3.157299, 2.525839, 2.020671], 'p_i': 80, 'u_i': 2.8041},
        {'id': 5, 'e_m': 10.333878, 'e_o_k': [8.037460, 6.429968], 'p_i': 40, 'u_i': 4.5045},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
