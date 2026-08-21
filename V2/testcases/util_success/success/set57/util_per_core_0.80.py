"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360014, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360014, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.402976, 'e_o_k': [0.035963, 0.028770, 0.023016, 0.018413, 0.014730], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 2.883659, 'e_o_k': [0.234490, 0.187592, 0.150073, 0.120059, 0.096047, 0.076838], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 17.323781, 'e_o_k': [2.887297, 2.309837], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 17.804345, 'e_o_k': [2.967391, 2.373913], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 11.987251, 'e_o_k': [1.997875, 1.598300], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 8.684826, 'e_o_k': [0.706221, 0.564977, 0.451982, 0.361585, 0.289268, 0.231415], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 2.602708, 'e_o_k': [0.433785, 0.347028], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 7.308664, 'e_o_k': [0.898606, 0.718885, 0.575108], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 191.360014
    return processors, tasks, B_BUDGET
