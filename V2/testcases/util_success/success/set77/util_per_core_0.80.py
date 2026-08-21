"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.36, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.36, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.878773, 'e_o_k': [0.071459, 0.057167, 0.045734, 0.036587, 0.029270, 0.023416], 'p_i': 10, 'u_i': 3.3901},
        {'id': 1, 'e_m': 6.762442, 'e_o_k': [0.549899, 0.439919, 0.351936, 0.281548, 0.225239, 0.180191], 'p_i': 20, 'u_i': 2.3217},
        {'id': 2, 'e_m': 9.002214, 'e_o_k': [0.914859, 0.731887, 0.585510, 0.468408], 'p_i': 40, 'u_i': 2.1118},
        {'id': 3, 'e_m': 2.593345, 'e_o_k': [0.263551, 0.210841, 0.168673, 0.134938], 'p_i': 80, 'u_i': 4.2305},
        {'id': 4, 'e_m': 29.075880, 'e_o_k': [4.845980, 3.876784], 'p_i': 80, 'u_i': 2.0791},
        {'id': 5, 'e_m': 15.896432, 'e_o_k': [2.649405, 2.119524], 'p_i': 80, 'u_i': 1.4810},
        {'id': 6, 'e_m': 14.472236, 'e_o_k': [2.412039, 1.929632], 'p_i': 80, 'u_i': 3.5439},
        {'id': 7, 'e_m': 1.734716, 'e_o_k': [0.141061, 0.112849, 0.090279, 0.072223, 0.057779, 0.046223], 'p_i': 10, 'u_i': 4.1958},
    ]
    B_BUDGET = 191.360000
    return processors, tasks, B_BUDGET
