"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.36, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.36, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.335265, 'e_o_k': [0.135698, 0.108558, 0.086847, 0.069477], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 2.045611, 'e_o_k': [0.207887, 0.166310, 0.133048, 0.106438], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 9.905314, 'e_o_k': [1.650886, 1.320709], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 15.055202, 'e_o_k': [1.851049, 1.480840, 1.184672], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 1.051846, 'e_o_k': [0.129325, 0.103460, 0.082768], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 31.402918, 'e_o_k': [5.233820, 4.187056], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 12.407257, 'e_o_k': [2.067876, 1.654301], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 15.948479, 'e_o_k': [2.658080, 2.126464], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 191.360000
    return processors, tasks, B_BUDGET
