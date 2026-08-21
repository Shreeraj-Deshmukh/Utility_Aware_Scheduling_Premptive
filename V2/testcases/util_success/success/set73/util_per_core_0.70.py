"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440007, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440007, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.368352, 'e_o_k': [0.728059, 0.582447], 'p_i': 10, 'u_i': 2.5346},
        {'id': 1, 'e_m': 5.363590, 'e_o_k': [0.659458, 0.527566, 0.422053], 'p_i': 20, 'u_i': 2.7749},
        {'id': 2, 'e_m': 11.952408, 'e_o_k': [0.971930, 0.777544, 0.622035, 0.497628, 0.398103, 0.318482], 'p_i': 40, 'u_i': 1.2098},
        {'id': 3, 'e_m': 2.179566, 'e_o_k': [0.267979, 0.214384, 0.171507], 'p_i': 80, 'u_i': 1.7928},
        {'id': 4, 'e_m': 2.434972, 'e_o_k': [0.198004, 0.158403, 0.126722, 0.101378, 0.081102, 0.064882], 'p_i': 20, 'u_i': 1.8586},
        {'id': 5, 'e_m': 6.131238, 'e_o_k': [0.753841, 0.603073, 0.482458], 'p_i': 40, 'u_i': 3.5571},
        {'id': 6, 'e_m': 3.367961, 'e_o_k': [0.273871, 0.219097, 0.175278, 0.140222, 0.112178, 0.089742], 'p_i': 40, 'u_i': 3.6967},
        {'id': 7, 'e_m': 0.194040, 'e_o_k': [0.023857, 0.019086, 0.015269], 'p_i': 20, 'u_i': 3.6040},
    ]
    B_BUDGET = 167.440007
    return processors, tasks, B_BUDGET
