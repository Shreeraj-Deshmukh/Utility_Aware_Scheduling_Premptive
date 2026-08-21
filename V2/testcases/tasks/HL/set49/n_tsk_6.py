"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400013, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400013, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.097167, 'e_o_k': [0.304769, 0.243815], 'p_i': 10, 'u_i': 1.7789},
        {'id': 1, 'e_m': 0.357025, 'e_o_k': [0.073161, 0.058529, 0.046823], 'p_i': 20, 'u_i': 1.0831},
        {'id': 2, 'e_m': 9.722762, 'e_o_k': [1.446151, 1.156921, 0.925537, 0.740429, 0.592343], 'p_i': 40, 'u_i': 3.5025},
        {'id': 3, 'e_m': 19.820506, 'e_o_k': [2.686230, 2.148984, 1.719187, 1.375350, 1.100280, 0.880224], 'p_i': 80, 'u_i': 3.4020},
        {'id': 4, 'e_m': 1.788974, 'e_o_k': [0.496937, 0.397550], 'p_i': 10, 'u_i': 4.4776},
        {'id': 5, 'e_m': 0.108372, 'e_o_k': [0.014687, 0.011750, 0.009400, 0.007520, 0.006016, 0.004813], 'p_i': 40, 'u_i': 3.0661},
    ]
    B_BUDGET = 110.400013
    return processors, tasks, B_BUDGET
