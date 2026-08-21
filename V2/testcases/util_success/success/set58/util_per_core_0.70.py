"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439995, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439995, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.203391, 'e_o_k': [0.179172, 0.143338, 0.114670, 0.091736, 0.073389, 0.058711], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 6.843641, 'e_o_k': [1.140607, 0.912486], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.971835, 'e_o_k': [0.119488, 0.095590, 0.076472], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 8.955382, 'e_o_k': [1.492564, 1.194051], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 1.454202, 'e_o_k': [0.147785, 0.118228, 0.094582, 0.075666], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 24.495597, 'e_o_k': [4.082600, 3.266080], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 2.322400, 'e_o_k': [0.236016, 0.188813, 0.151050, 0.120840], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.173856, 'e_o_k': [0.017668, 0.014135, 0.011308, 0.009046], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 167.439995
    return processors, tasks, B_BUDGET
