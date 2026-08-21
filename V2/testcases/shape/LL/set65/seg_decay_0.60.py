"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.063904, 'e_o_k': [0.014684, 0.008810, 0.005286, 0.003172], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 2.319143, 'e_o_k': [0.591618, 0.354971, 0.212983], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.400395, 'e_o_k': [0.102142, 0.061285, 0.036771], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 4.718930, 'e_o_k': [1.203809, 0.722285, 0.433371], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 1.741564, 'e_o_k': [0.400176, 0.240105, 0.144063, 0.086438], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 7.261818, 'e_o_k': [1.523441, 0.914065, 0.548439, 0.329063, 0.197438, 0.118463], 'p_i': 80, 'u_i': 1.3665},
        {'id': 6, 'e_m': 0.036678, 'e_o_k': [0.008428, 0.005057, 0.003034, 0.001820], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 0.579422, 'e_o_k': [0.125655, 0.075393, 0.045236, 0.027142, 0.016285], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
