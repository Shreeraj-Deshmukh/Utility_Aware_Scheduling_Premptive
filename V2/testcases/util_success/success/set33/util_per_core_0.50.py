"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600018, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600018, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.060241, 'e_o_k': [0.007407, 0.005925, 0.004740], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 4.560064, 'e_o_k': [0.560664, 0.448531, 0.358825], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 7.015270, 'e_o_k': [0.862533, 0.690027, 0.552021], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 1.204055, 'e_o_k': [0.200676, 0.160541], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 6.804313, 'e_o_k': [0.607239, 0.485791, 0.388633, 0.310906, 0.248725], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 1.703274, 'e_o_k': [0.152006, 0.121605, 0.097284, 0.077827, 0.062262], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 1.532398, 'e_o_k': [0.255400, 0.204320], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 3.667378, 'e_o_k': [0.372701, 0.298161, 0.238529, 0.190823], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 119.600018
    return processors, tasks, B_BUDGET
