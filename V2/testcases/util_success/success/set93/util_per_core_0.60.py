"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.717816, 'e_o_k': [0.174575, 0.139660, 0.111728, 0.089382], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 1.696658, 'e_o_k': [0.137967, 0.110373, 0.088299, 0.070639, 0.056511, 0.045209], 'p_i': 20, 'u_i': 1.5082},
        {'id': 2, 'e_m': 2.453639, 'e_o_k': [0.249354, 0.199483, 0.159586, 0.127669], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 15.374459, 'e_o_k': [1.562445, 1.249956, 0.999965, 0.799972], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 6.350868, 'e_o_k': [0.516431, 0.413145, 0.330516, 0.264413, 0.211530, 0.169224], 'p_i': 20, 'u_i': 2.1026},
        {'id': 5, 'e_m': 0.656196, 'e_o_k': [0.053360, 0.042688, 0.034150, 0.027320, 0.021856, 0.017485], 'p_i': 10, 'u_i': 4.2691},
        {'id': 6, 'e_m': 3.140909, 'e_o_k': [0.255408, 0.204327, 0.163461, 0.130769, 0.104615, 0.083692], 'p_i': 20, 'u_i': 3.6679},
        {'id': 7, 'e_m': 11.972428, 'e_o_k': [1.995405, 1.596324], 'p_i': 80, 'u_i': 2.7165},
    ]
    B_BUDGET = 143.520000
    return processors, tasks, B_BUDGET
