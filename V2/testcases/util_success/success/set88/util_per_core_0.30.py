"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759987, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759987, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.514908, 'e_o_k': [0.063308, 0.050647, 0.040517], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 1.187054, 'e_o_k': [0.197842, 0.158274], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 3.830353, 'e_o_k': [0.389264, 0.311411, 0.249129, 0.199303], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.169342, 'e_o_k': [0.017210, 0.013768, 0.011014, 0.008811], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 7.521303, 'e_o_k': [0.671225, 0.536980, 0.429584, 0.343667, 0.274934], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 4.043128, 'e_o_k': [0.328774, 0.263019, 0.210415, 0.168332, 0.134666, 0.107733], 'p_i': 40, 'u_i': 4.5618},
        {'id': 6, 'e_m': 0.199790, 'e_o_k': [0.033298, 0.026639], 'p_i': 10, 'u_i': 3.9189},
        {'id': 7, 'e_m': 3.287642, 'e_o_k': [0.334110, 0.267288, 0.213830, 0.171064], 'p_i': 40, 'u_i': 2.1344},
    ]
    B_BUDGET = 71.759987
    return processors, tasks, B_BUDGET
