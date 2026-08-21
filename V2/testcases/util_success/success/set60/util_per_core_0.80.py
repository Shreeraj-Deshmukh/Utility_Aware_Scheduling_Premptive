"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359999, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359999, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.567149, 'e_o_k': [0.229101, 0.183281, 0.146624, 0.117300, 0.093840], 'p_i': 10, 'u_i': 4.7898},
        {'id': 1, 'e_m': 8.260651, 'e_o_k': [0.737207, 0.589766, 0.471813, 0.377450, 0.301960], 'p_i': 20, 'u_i': 3.8151},
        {'id': 2, 'e_m': 2.427088, 'e_o_k': [0.246655, 0.197324, 0.157859, 0.126287], 'p_i': 40, 'u_i': 2.4922},
        {'id': 3, 'e_m': 10.418638, 'e_o_k': [0.847209, 0.677767, 0.542214, 0.433771, 0.347017, 0.277613], 'p_i': 80, 'u_i': 2.2134},
        {'id': 4, 'e_m': 4.528619, 'e_o_k': [0.556797, 0.445438, 0.356350], 'p_i': 20, 'u_i': 4.2486},
        {'id': 5, 'e_m': 0.818447, 'e_o_k': [0.066553, 0.053243, 0.042594, 0.034075, 0.027260, 0.021808], 'p_i': 10, 'u_i': 3.7555},
        {'id': 6, 'e_m': 3.947310, 'e_o_k': [0.657885, 0.526308], 'p_i': 20, 'u_i': 3.0652},
        {'id': 7, 'e_m': 2.337012, 'e_o_k': [0.389502, 0.311602], 'p_i': 10, 'u_i': 3.3025},
    ]
    B_BUDGET = 191.359999
    return processors, tasks, B_BUDGET
