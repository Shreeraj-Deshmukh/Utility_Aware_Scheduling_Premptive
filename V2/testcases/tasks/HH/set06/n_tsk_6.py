"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.527669, 'e_o_k': [0.579717, 0.463773, 0.371019, 0.296815, 0.237452, 0.189962], 'p_i': 10, 'u_i': 4.5754},
        {'id': 1, 'e_m': 3.993502, 'e_o_k': [1.893937, 1.515150, 1.212120, 0.969696], 'p_i': 20, 'u_i': 3.5388},
        {'id': 2, 'e_m': 13.759506, 'e_o_k': [5.221428, 4.177142, 3.341714, 2.673371, 2.138697, 1.710957], 'p_i': 40, 'u_i': 1.2818},
        {'id': 3, 'e_m': 0.291706, 'e_o_k': [0.226882, 0.181506], 'p_i': 80, 'u_i': 2.2300},
        {'id': 4, 'e_m': 0.676970, 'e_o_k': [0.321056, 0.256845, 0.205476, 0.164381], 'p_i': 10, 'u_i': 1.1980},
        {'id': 5, 'e_m': 0.644539, 'e_o_k': [0.305676, 0.244540, 0.195632, 0.156506], 'p_i': 20, 'u_i': 3.9540},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
