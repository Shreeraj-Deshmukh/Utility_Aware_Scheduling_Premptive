"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120006, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120006, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.848384, 'e_o_k': [0.150304, 0.120244, 0.096195, 0.076956, 0.061565, 0.049252], 'p_i': 10, 'u_i': 1.9884},
        {'id': 1, 'e_m': 4.914841, 'e_o_k': [0.604284, 0.483427, 0.386742], 'p_i': 20, 'u_i': 4.7767},
        {'id': 2, 'e_m': 1.633160, 'e_o_k': [0.165972, 0.132777, 0.106222, 0.084977], 'p_i': 40, 'u_i': 2.3478},
        {'id': 3, 'e_m': 39.627773, 'e_o_k': [4.872267, 3.897814, 3.118251], 'p_i': 80, 'u_i': 2.9933},
        {'id': 4, 'e_m': 33.434748, 'e_o_k': [5.572458, 4.457966], 'p_i': 80, 'u_i': 1.6969},
        {'id': 5, 'e_m': 25.392117, 'e_o_k': [2.580500, 2.064400, 1.651520, 1.321216], 'p_i': 80, 'u_i': 1.2841},
        {'id': 6, 'e_m': 1.665636, 'e_o_k': [0.204791, 0.163833, 0.131066], 'p_i': 40, 'u_i': 3.9852},
        {'id': 7, 'e_m': 36.501332, 'e_o_k': [3.709485, 2.967588, 2.374070, 1.899256], 'p_i': 80, 'u_i': 4.0749},
    ]
    B_BUDGET = 263.120006
    return processors, tasks, B_BUDGET
