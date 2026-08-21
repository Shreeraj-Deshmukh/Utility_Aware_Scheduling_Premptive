"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359979, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359979, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.993504, 'e_o_k': [0.177907, 0.142325, 0.113860, 0.091088, 0.072871], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 1.188039, 'e_o_k': [0.146070, 0.116856, 0.093485], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 3.565093, 'e_o_k': [0.318160, 0.254528, 0.203623, 0.162898, 0.130318], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 9.318040, 'e_o_k': [0.831572, 0.665257, 0.532206, 0.425765, 0.340612], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 1.748454, 'e_o_k': [0.142178, 0.113743, 0.090994, 0.072795, 0.058236, 0.046589], 'p_i': 20, 'u_i': 3.3809},
        {'id': 5, 'e_m': 36.650460, 'e_o_k': [3.724640, 2.979712, 2.383770, 1.907016], 'p_i': 80, 'u_i': 4.9290},
        {'id': 6, 'e_m': 3.106429, 'e_o_k': [0.517738, 0.414191], 'p_i': 20, 'u_i': 1.8035},
        {'id': 7, 'e_m': 4.347699, 'e_o_k': [0.441839, 0.353471, 0.282777, 0.226222], 'p_i': 10, 'u_i': 3.4846},
    ]
    B_BUDGET = 191.359979
    return processors, tasks, B_BUDGET
