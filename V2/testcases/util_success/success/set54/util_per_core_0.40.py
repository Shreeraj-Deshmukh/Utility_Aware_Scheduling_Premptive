"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680013, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680013, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.060089, 'e_o_k': [0.253290, 0.202632, 0.162105], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.339026, 'e_o_k': [0.034454, 0.027563, 0.022050, 0.017640], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 15.847193, 'e_o_k': [1.610487, 1.288390, 1.030712, 0.824569], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 1.762893, 'e_o_k': [0.157326, 0.125861, 0.100689, 0.080551, 0.064441], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.784991, 'e_o_k': [0.096515, 0.077212, 0.061770], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.814426, 'e_o_k': [0.082767, 0.066214, 0.052971, 0.042377], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.165452, 'e_o_k': [0.014766, 0.011812, 0.009450, 0.007560, 0.006048], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.989677, 'e_o_k': [0.100577, 0.080462, 0.064369, 0.051495], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 95.680013
    return processors, tasks, B_BUDGET
