"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519993, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519993, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.470930, 'e_o_k': [0.200928, 0.160742, 0.128594, 0.102875, 0.082300, 0.065840], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.051450, 'e_o_k': [0.005229, 0.004183, 0.003346, 0.002677], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 4.388837, 'e_o_k': [0.731473, 0.585178], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 2.482862, 'e_o_k': [0.305270, 0.244216, 0.195373], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 1.467187, 'e_o_k': [0.130936, 0.104749, 0.083799, 0.067039, 0.053632], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 2.802469, 'e_o_k': [0.284804, 0.227843, 0.182274, 0.145819], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 23.149524, 'e_o_k': [2.352594, 1.882075, 1.505660, 1.204528], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 15.071507, 'e_o_k': [1.853054, 1.482443, 1.185955], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 143.519993
    return processors, tasks, B_BUDGET
