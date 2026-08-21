"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 60.720007, "H": 80, "J": 22, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.3, "seed": 1069, "set": 69, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.30"}
"""

_SPEC = '{"B": 60.720007, "H": 80, "J": 22, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.3, "seed": 1069, "set": 69, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.028851, 'e_o_k': [0.005912, 0.004730, 0.003784], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 0.425044, 'e_o_k': [0.118068, 0.094454], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.371477, 'e_o_k': [0.055253, 0.044202, 0.035362, 0.028290, 0.022632], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 3.599048, 'e_o_k': [0.737510, 0.590008, 0.472006], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 5.420557, 'e_o_k': [0.806247, 0.644997, 0.515998, 0.412798, 0.330239], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 15.171358, 'e_o_k': [3.108885, 2.487108, 1.989686], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 0.633743, 'e_o_k': [0.107341, 0.085873, 0.068698, 0.054959], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 2.600128, 'e_o_k': [0.722258, 0.577806], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 60.720007
    return processors, tasks, B_BUDGET
