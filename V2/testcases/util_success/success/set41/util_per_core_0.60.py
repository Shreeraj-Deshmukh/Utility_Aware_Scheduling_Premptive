"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520005, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520005, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.145383, 'e_o_k': [0.011822, 0.009458, 0.007566, 0.006053, 0.004842, 0.003874], 'p_i': 10, 'u_i': 3.2508},
        {'id': 1, 'e_m': 0.743609, 'e_o_k': [0.091427, 0.073142, 0.058513], 'p_i': 20, 'u_i': 3.3334},
        {'id': 2, 'e_m': 5.619724, 'e_o_k': [0.936621, 0.749297], 'p_i': 40, 'u_i': 2.1081},
        {'id': 3, 'e_m': 0.999454, 'e_o_k': [0.089194, 0.071356, 0.057084, 0.045668, 0.036534], 'p_i': 80, 'u_i': 1.8691},
        {'id': 4, 'e_m': 5.665956, 'e_o_k': [0.505648, 0.404518, 0.323615, 0.258892, 0.207113], 'p_i': 80, 'u_i': 3.0834},
        {'id': 5, 'e_m': 2.996976, 'e_o_k': [0.304571, 0.243657, 0.194925, 0.155940], 'p_i': 10, 'u_i': 3.6806},
        {'id': 6, 'e_m': 38.813441, 'e_o_k': [3.463836, 2.771069, 2.216855, 1.773484, 1.418787], 'p_i': 80, 'u_i': 3.6556},
        {'id': 7, 'e_m': 2.792100, 'e_o_k': [0.227044, 0.181635, 0.145308, 0.116247, 0.092997, 0.074398], 'p_i': 20, 'u_i': 4.7806},
    ]
    B_BUDGET = 143.520005
    return processors, tasks, B_BUDGET
