"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200005, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200005, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.669082, 'e_o_k': [0.169622, 0.135698, 0.108558, 0.086847], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 2.557013, 'e_o_k': [0.259859, 0.207887, 0.166310, 0.133048], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 12.381642, 'e_o_k': [2.063607, 1.650886], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 18.819002, 'e_o_k': [2.313812, 1.851049, 1.480840], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 1.314808, 'e_o_k': [0.161657, 0.129325, 0.103460], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 39.253648, 'e_o_k': [6.542275, 5.233820], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 15.509072, 'e_o_k': [2.584845, 2.067876], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 19.935598, 'e_o_k': [3.322600, 2.658080], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 239.200005
    return processors, tasks, B_BUDGET
