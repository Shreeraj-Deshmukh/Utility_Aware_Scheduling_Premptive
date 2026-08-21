"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.165446, 'e_o_k': [0.068903, 0.055122, 0.044098, 0.035278, 0.028223], 'p_i': 10, 'u_i': 3.5312},
        {'id': 1, 'e_m': 1.641715, 'e_o_k': [0.622994, 0.498396, 0.398716, 0.318973, 0.255179, 0.204143], 'p_i': 20, 'u_i': 1.4207},
        {'id': 2, 'e_m': 5.181947, 'e_o_k': [2.158117, 1.726494, 1.381195, 1.104956, 0.883965], 'p_i': 40, 'u_i': 4.1417},
        {'id': 3, 'e_m': 10.738436, 'e_o_k': [4.472219, 3.577775, 2.862220, 2.289776, 1.831821], 'p_i': 80, 'u_i': 4.9795},
        {'id': 4, 'e_m': 0.202795, 'e_o_k': [0.116358, 0.093086, 0.074469], 'p_i': 20, 'u_i': 4.9448},
        {'id': 5, 'e_m': 0.274508, 'e_o_k': [0.114324, 0.091459, 0.073167, 0.058534, 0.046827], 'p_i': 10, 'u_i': 4.4554},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
