"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.966054, 'e_o_k': [0.130927, 0.104742, 0.083793, 0.067035, 0.053628, 0.042902], 'p_i': 10, 'u_i': 2.1800},
        {'id': 1, 'e_m': 0.002627, 'e_o_k': [0.000356, 0.000285, 0.000228, 0.000182, 0.000146, 0.000117], 'p_i': 20, 'u_i': 3.3278},
        {'id': 2, 'e_m': 11.582843, 'e_o_k': [1.961864, 1.569491, 1.255593, 1.004474], 'p_i': 40, 'u_i': 2.2754},
        {'id': 3, 'e_m': 1.095371, 'e_o_k': [0.304270, 0.243416], 'p_i': 80, 'u_i': 1.2102},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
