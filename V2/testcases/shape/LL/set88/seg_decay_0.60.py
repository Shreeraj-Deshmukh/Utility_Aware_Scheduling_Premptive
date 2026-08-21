"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200013, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200013, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.343272, 'e_o_k': [0.087569, 0.052542, 0.031525], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 0.791370, 'e_o_k': [0.247303, 0.148382], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 2.553569, 'e_o_k': [0.586757, 0.352054, 0.211233, 0.126740], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.112895, 'e_o_k': [0.025941, 0.015565, 0.009339, 0.005603], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 5.014202, 'e_o_k': [1.087396, 0.652438, 0.391463, 0.234878, 0.140927], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 2.695419, 'e_o_k': [0.565466, 0.339280, 0.203568, 0.122141, 0.073284, 0.043971], 'p_i': 40, 'u_i': 4.5618},
        {'id': 6, 'e_m': 0.133194, 'e_o_k': [0.041623, 0.024974], 'p_i': 10, 'u_i': 3.9189},
        {'id': 7, 'e_m': 2.191761, 'e_o_k': [0.503622, 0.302173, 0.181304, 0.108782], 'p_i': 40, 'u_i': 2.1344},
    ]
    B_BUDGET = 55.200013
    return processors, tasks, B_BUDGET
