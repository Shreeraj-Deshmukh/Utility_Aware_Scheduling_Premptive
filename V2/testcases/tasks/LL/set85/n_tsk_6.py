"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.337681, 'e_o_k': [0.093800, 0.075040], 'p_i': 10, 'u_i': 2.3226},
        {'id': 1, 'e_m': 0.665720, 'e_o_k': [0.184922, 0.147938], 'p_i': 20, 'u_i': 1.3159},
        {'id': 2, 'e_m': 1.752171, 'e_o_k': [0.486714, 0.389371], 'p_i': 40, 'u_i': 2.3324},
        {'id': 3, 'e_m': 3.971126, 'e_o_k': [0.590660, 0.472528, 0.378022, 0.302418, 0.241934], 'p_i': 80, 'u_i': 2.7878},
        {'id': 4, 'e_m': 0.688605, 'e_o_k': [0.141107, 0.112886, 0.090309], 'p_i': 40, 'u_i': 1.7467},
        {'id': 5, 'e_m': 2.222875, 'e_o_k': [0.301261, 0.241009, 0.192807, 0.154246, 0.123397, 0.098717], 'p_i': 10, 'u_i': 1.9890},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
