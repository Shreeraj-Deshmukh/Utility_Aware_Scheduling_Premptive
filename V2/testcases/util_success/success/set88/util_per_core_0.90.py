"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.517056, 'e_o_k': [0.309474, 0.247579, 0.198063], 'p_i': 10, 'u_i': 2.7501},
        {'id': 1, 'e_m': 6.221226, 'e_o_k': [0.555202, 0.444162, 0.355329, 0.284264, 0.227411], 'p_i': 20, 'u_i': 3.0723},
        {'id': 2, 'e_m': 19.022668, 'e_o_k': [1.546860, 1.237488, 0.989991, 0.791992, 0.633594, 0.506875], 'p_i': 40, 'u_i': 1.3696},
        {'id': 3, 'e_m': 20.701346, 'e_o_k': [2.545247, 2.036198, 1.628958], 'p_i': 80, 'u_i': 4.6022},
        {'id': 4, 'e_m': 19.159926, 'e_o_k': [1.947147, 1.557718, 1.246174, 0.996939], 'p_i': 80, 'u_i': 2.1344},
        {'id': 5, 'e_m': 3.942898, 'e_o_k': [0.657150, 0.525720], 'p_i': 20, 'u_i': 2.5225},
        {'id': 6, 'e_m': 1.986139, 'e_o_k': [0.244197, 0.195358, 0.156286], 'p_i': 40, 'u_i': 4.3404},
        {'id': 7, 'e_m': 1.328175, 'e_o_k': [0.134977, 0.107982, 0.086385, 0.069108], 'p_i': 80, 'u_i': 2.9431},
    ]
    B_BUDGET = 215.280000
    return processors, tasks, B_BUDGET
