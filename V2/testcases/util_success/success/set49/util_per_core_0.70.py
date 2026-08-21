"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439977, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439977, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.448666, 'e_o_k': [0.199117, 0.159294, 0.127435, 0.101948, 0.081558, 0.065247], 'p_i': 10, 'u_i': 3.0661},
        {'id': 1, 'e_m': 5.760721, 'e_o_k': [0.468443, 0.374754, 0.299803, 0.239843, 0.191874, 0.153499], 'p_i': 20, 'u_i': 2.9486},
        {'id': 2, 'e_m': 19.725925, 'e_o_k': [3.287654, 2.630123], 'p_i': 40, 'u_i': 3.9206},
        {'id': 3, 'e_m': 12.528627, 'e_o_k': [1.273235, 1.018588, 0.814870, 0.651896], 'p_i': 80, 'u_i': 3.4151},
        {'id': 4, 'e_m': 2.827201, 'e_o_k': [0.287317, 0.229854, 0.183883, 0.147106], 'p_i': 40, 'u_i': 2.3956},
        {'id': 5, 'e_m': 6.555523, 'e_o_k': [0.585036, 0.468029, 0.374423, 0.299538, 0.239631], 'p_i': 80, 'u_i': 3.6029},
        {'id': 6, 'e_m': 0.512164, 'e_o_k': [0.052049, 0.041639, 0.033311, 0.026649], 'p_i': 10, 'u_i': 4.4783},
        {'id': 7, 'e_m': 0.540036, 'e_o_k': [0.090006, 0.072005], 'p_i': 40, 'u_i': 1.4735},
    ]
    B_BUDGET = 167.439977
    return processors, tasks, B_BUDGET
