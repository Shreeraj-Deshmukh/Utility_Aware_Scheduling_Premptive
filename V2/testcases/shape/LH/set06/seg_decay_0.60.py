"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.561850, 'e_o_k': [0.491619, 0.294971], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 1.499211, 'e_o_k': [0.964566, 0.578740, 0.347244, 0.208346], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 6.285193, 'e_o_k': [4.043782, 2.426269, 1.455762, 0.873457], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.158746, 'e_o_k': [0.138903, 0.083342], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 1.379315, 'e_o_k': [0.887427, 0.532456, 0.319474, 0.191684], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 1.465455, 'e_o_k': [1.282273, 0.769364], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.015684, 'e_o_k': [0.009524, 0.005714, 0.003429, 0.002057, 0.001234], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.033297, 'e_o_k': [0.020219, 0.012131, 0.007279, 0.004367, 0.002620], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
