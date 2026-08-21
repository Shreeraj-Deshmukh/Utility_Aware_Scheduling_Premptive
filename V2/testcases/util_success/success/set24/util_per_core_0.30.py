"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759985, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759985, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.191314, 'e_o_k': [0.017073, 0.013659, 0.010927, 0.008742, 0.006993], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 1.325197, 'e_o_k': [0.162934, 0.130347, 0.104278], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 3.538347, 'e_o_k': [0.315773, 0.252619, 0.202095, 0.161676, 0.129341], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 1.557452, 'e_o_k': [0.158278, 0.126622, 0.101298, 0.081038], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.735301, 'e_o_k': [0.059792, 0.047834, 0.038267, 0.030614, 0.024491, 0.019593], 'p_i': 40, 'u_i': 1.3531},
        {'id': 5, 'e_m': 21.219318, 'e_o_k': [3.536553, 2.829242], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.599440, 'e_o_k': [0.099907, 0.079925], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 1.262277, 'e_o_k': [0.128280, 0.102624, 0.082099, 0.065679], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 71.759985
    return processors, tasks, B_BUDGET
