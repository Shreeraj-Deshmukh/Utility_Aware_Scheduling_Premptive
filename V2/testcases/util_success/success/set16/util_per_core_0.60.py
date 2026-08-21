"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.609814, 'e_o_k': [0.130905, 0.104724, 0.083779, 0.067023, 0.053619, 0.042895], 'p_i': 10, 'u_i': 3.0333},
        {'id': 1, 'e_m': 3.014733, 'e_o_k': [0.245148, 0.196118, 0.156895, 0.125516, 0.100413, 0.080330], 'p_i': 20, 'u_i': 1.6855},
        {'id': 2, 'e_m': 6.750634, 'e_o_k': [0.602448, 0.481959, 0.385567, 0.308454, 0.246763], 'p_i': 40, 'u_i': 1.7213},
        {'id': 3, 'e_m': 7.761185, 'e_o_k': [0.631114, 0.504891, 0.403913, 0.323130, 0.258504, 0.206803], 'p_i': 80, 'u_i': 2.0710},
        {'id': 4, 'e_m': 6.811821, 'e_o_k': [0.692258, 0.553807, 0.443045, 0.354436], 'p_i': 80, 'u_i': 2.4462},
        {'id': 5, 'e_m': 1.028596, 'e_o_k': [0.104532, 0.083626, 0.066901, 0.053520], 'p_i': 10, 'u_i': 2.4016},
        {'id': 6, 'e_m': 22.644171, 'e_o_k': [2.784119, 2.227296, 1.781836], 'p_i': 80, 'u_i': 3.4602},
        {'id': 7, 'e_m': 12.115343, 'e_o_k': [1.231234, 0.984987, 0.787990, 0.630392], 'p_i': 80, 'u_i': 3.9709},
    ]
    B_BUDGET = 143.520010
    return processors, tasks, B_BUDGET
