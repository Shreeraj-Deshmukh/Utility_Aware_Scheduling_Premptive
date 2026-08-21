"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440007, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440007, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.449111, 'e_o_k': [0.055219, 0.044175, 0.035340], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.945133, 'e_o_k': [0.076855, 0.061484, 0.049187, 0.039350, 0.031480, 0.025184], 'p_i': 20, 'u_i': 3.1493},
        {'id': 2, 'e_m': 1.327791, 'e_o_k': [0.134938, 0.107951, 0.086360, 0.069088], 'p_i': 40, 'u_i': 4.3022},
        {'id': 3, 'e_m': 28.344059, 'e_o_k': [2.304845, 1.843876, 1.475101, 1.180081, 0.944064, 0.755252], 'p_i': 80, 'u_i': 4.8493},
        {'id': 4, 'e_m': 17.729579, 'e_o_k': [2.954930, 2.363944], 'p_i': 40, 'u_i': 1.1754},
        {'id': 5, 'e_m': 10.648651, 'e_o_k': [0.865913, 0.692730, 0.554184, 0.443347, 0.354678, 0.283742], 'p_i': 40, 'u_i': 3.0798},
        {'id': 6, 'e_m': 1.444169, 'e_o_k': [0.177562, 0.142049, 0.113639], 'p_i': 10, 'u_i': 3.4237},
        {'id': 7, 'e_m': 1.329283, 'e_o_k': [0.108093, 0.086474, 0.069179, 0.055344, 0.044275, 0.035420], 'p_i': 20, 'u_i': 3.1726},
    ]
    B_BUDGET = 167.440007
    return processors, tasks, B_BUDGET
