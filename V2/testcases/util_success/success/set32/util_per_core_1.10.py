"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.982253, 'e_o_k': [0.497042, 0.397634], 'p_i': 10, 'u_i': 2.4344},
        {'id': 1, 'e_m': 9.173556, 'e_o_k': [0.818678, 0.654942, 0.523954, 0.419163, 0.335330], 'p_i': 20, 'u_i': 4.3497},
        {'id': 2, 'e_m': 10.149919, 'e_o_k': [1.691653, 1.353323], 'p_i': 40, 'u_i': 1.9085},
        {'id': 3, 'e_m': 38.028407, 'e_o_k': [3.092344, 2.473875, 1.979100, 1.583280, 1.266624, 1.013299], 'p_i': 80, 'u_i': 4.5985},
        {'id': 4, 'e_m': 2.024887, 'e_o_k': [0.248962, 0.199169, 0.159335], 'p_i': 10, 'u_i': 1.1568},
        {'id': 5, 'e_m': 0.332547, 'e_o_k': [0.033795, 0.027036, 0.021629, 0.017303], 'p_i': 40, 'u_i': 3.3218},
        {'id': 6, 'e_m': 19.601230, 'e_o_k': [1.593907, 1.275126, 1.020100, 0.816080, 0.652864, 0.522291], 'p_i': 40, 'u_i': 3.9399},
        {'id': 7, 'e_m': 0.526429, 'e_o_k': [0.087738, 0.070191], 'p_i': 40, 'u_i': 2.8364},
    ]
    B_BUDGET = 263.119999
    return processors, tasks, B_BUDGET
