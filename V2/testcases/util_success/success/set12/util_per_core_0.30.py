"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759993, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759993, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.860262, 'e_o_k': [0.143377, 0.114702], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 2.830316, 'e_o_k': [0.471719, 0.377376], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 4.012858, 'e_o_k': [0.493384, 0.394707, 0.315766], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 12.726935, 'e_o_k': [1.135793, 0.908634, 0.726907, 0.581526, 0.465221], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 0.824623, 'e_o_k': [0.101388, 0.081110, 0.064888], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.111723, 'e_o_k': [0.009971, 0.007976, 0.006381, 0.005105, 0.004084], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 2.473434, 'e_o_k': [0.201131, 0.160905, 0.128724, 0.102979, 0.082383, 0.065907], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 2.825167, 'e_o_k': [0.252127, 0.201702, 0.161361, 0.129089, 0.103271], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 71.759993
    return processors, tasks, B_BUDGET
