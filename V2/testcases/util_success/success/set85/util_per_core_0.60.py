"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519984, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519984, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.732660, 'e_o_k': [0.122110, 0.097688], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 1.386983, 'e_o_k': [0.140954, 0.112763, 0.090210, 0.072168], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 3.432490, 'e_o_k': [0.306326, 0.245061, 0.196049, 0.156839, 0.125471], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 6.985815, 'e_o_k': [0.858912, 0.687129, 0.549704], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.217151, 'e_o_k': [0.017658, 0.014126, 0.011301, 0.009041, 0.007233, 0.005786], 'p_i': 10, 'u_i': 1.9890},
        {'id': 5, 'e_m': 0.211431, 'e_o_k': [0.025996, 0.020797, 0.016637], 'p_i': 40, 'u_i': 1.7667},
        {'id': 6, 'e_m': 7.387009, 'e_o_k': [0.908239, 0.726591, 0.581273], 'p_i': 20, 'u_i': 2.7743},
        {'id': 7, 'e_m': 4.878985, 'e_o_k': [0.495832, 0.396665, 0.317332, 0.253866], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 143.519984
    return processors, tasks, B_BUDGET
