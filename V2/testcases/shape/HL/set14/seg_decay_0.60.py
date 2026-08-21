"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.722458, 'e_o_k': [0.225768, 0.135461], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 3.086888, 'e_o_k': [0.787471, 0.472483, 0.283490], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 11.212672, 'e_o_k': [2.860376, 1.716225, 1.029735], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 4.466066, 'e_o_k': [1.139302, 0.683581, 0.410149], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.168840, 'e_o_k': [0.038796, 0.023278, 0.013967, 0.008380], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 1.988081, 'e_o_k': [0.417075, 0.250245, 0.150147, 0.090088, 0.054053, 0.032432], 'p_i': 40, 'u_i': 1.9821},
        {'id': 6, 'e_m': 7.911221, 'e_o_k': [2.018169, 1.210901, 0.726541], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 6.925151, 'e_o_k': [1.591257, 0.954754, 0.572853, 0.343712], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
