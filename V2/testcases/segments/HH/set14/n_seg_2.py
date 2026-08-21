"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640007, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640007, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.722458, 'e_o_k': [0.561912, 0.449530], 'p_i': 10, 'u_i': 1.0216},
        {'id': 1, 'e_m': 3.086888, 'e_o_k': [2.400913, 1.920730], 'p_i': 20, 'u_i': 4.0085},
        {'id': 2, 'e_m': 11.212672, 'e_o_k': [8.720967, 6.976774], 'p_i': 40, 'u_i': 1.9931},
        {'id': 3, 'e_m': 4.466066, 'e_o_k': [3.473607, 2.778885], 'p_i': 80, 'u_i': 2.4773},
        {'id': 4, 'e_m': 0.168840, 'e_o_k': [0.131320, 0.105056], 'p_i': 80, 'u_i': 3.1022},
        {'id': 5, 'e_m': 1.988081, 'e_o_k': [1.546285, 1.237028], 'p_i': 40, 'u_i': 1.7440},
        {'id': 6, 'e_m': 7.911221, 'e_o_k': [6.153172, 4.922538], 'p_i': 80, 'u_i': 1.2190},
        {'id': 7, 'e_m': 6.925151, 'e_o_k': [5.386229, 4.308983], 'p_i': 80, 'u_i': 2.8489},
    ]
    B_BUDGET = 176.640007
    return processors, tasks, B_BUDGET
