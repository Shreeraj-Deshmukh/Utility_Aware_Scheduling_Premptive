"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.561850, 'e_o_k': [0.175578, 0.105347], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 1.499211, 'e_o_k': [0.344488, 0.206693, 0.124016, 0.074409], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 6.285193, 'e_o_k': [1.444208, 0.866525, 0.519915, 0.311949], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.158746, 'e_o_k': [0.049608, 0.029765], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 1.379315, 'e_o_k': [0.316938, 0.190163, 0.114098, 0.068459], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 1.465455, 'e_o_k': [0.457955, 0.274773], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.015684, 'e_o_k': [0.003401, 0.002041, 0.001224, 0.000735, 0.000441], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.033297, 'e_o_k': [0.007221, 0.004333, 0.002600, 0.001560, 0.000936], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
