"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.112614, 'e_o_k': [0.013846, 0.011077, 0.008861], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 0.686888, 'e_o_k': [0.114481, 0.091585], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 2.172776, 'e_o_k': [0.362129, 0.289703], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 4.314900, 'e_o_k': [0.438506, 0.350805, 0.280644, 0.224515], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.380745, 'e_o_k': [0.038694, 0.030955, 0.024764, 0.019811], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 8.014622, 'e_o_k': [0.985404, 0.788323, 0.630659], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 2.193961, 'e_o_k': [0.222964, 0.178371, 0.142697, 0.114157], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 23.078811, 'e_o_k': [2.837559, 2.270047, 1.816038], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 95.680001
    return processors, tasks, B_BUDGET
