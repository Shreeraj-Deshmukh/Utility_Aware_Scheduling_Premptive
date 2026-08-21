"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520009, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520009, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.383463, 'e_o_k': [0.031182, 0.024946, 0.019956, 0.015965, 0.012772, 0.010218], 'p_i': 10, 'u_i': 4.5169},
        {'id': 1, 'e_m': 8.752404, 'e_o_k': [1.458734, 1.166987], 'p_i': 20, 'u_i': 3.9484},
        {'id': 2, 'e_m': 1.545045, 'e_o_k': [0.137885, 0.110308, 0.088246, 0.070597, 0.056478], 'p_i': 40, 'u_i': 3.8598},
        {'id': 3, 'e_m': 1.987556, 'e_o_k': [0.161621, 0.129297, 0.103438, 0.082750, 0.066200, 0.052960], 'p_i': 80, 'u_i': 3.9484},
        {'id': 4, 'e_m': 29.051813, 'e_o_k': [3.571944, 2.857555, 2.286044], 'p_i': 80, 'u_i': 4.6365},
        {'id': 5, 'e_m': 0.594878, 'e_o_k': [0.048374, 0.038699, 0.030959, 0.024767, 0.019814, 0.015851], 'p_i': 40, 'u_i': 4.7054},
        {'id': 6, 'e_m': 4.839492, 'e_o_k': [0.806582, 0.645266], 'p_i': 80, 'u_i': 3.2554},
        {'id': 7, 'e_m': 4.440994, 'e_o_k': [0.740166, 0.592133], 'p_i': 20, 'u_i': 3.5452},
    ]
    B_BUDGET = 143.520009
    return processors, tasks, B_BUDGET
