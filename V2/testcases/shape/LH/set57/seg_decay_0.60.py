"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319984, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319984, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100744, 'e_o_k': [0.061173, 0.036704, 0.022022, 0.013213, 0.007928], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 0.720915, 'e_o_k': [0.423470, 0.254082, 0.152449, 0.091469, 0.054882, 0.032929], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 4.330945, 'e_o_k': [3.789577, 2.273746], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 4.451086, 'e_o_k': [3.894700, 2.336820], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 2.996813, 'e_o_k': [2.622211, 1.573327], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 2.171206, 'e_o_k': [1.275380, 0.765228, 0.459137, 0.275482, 0.165289, 0.099174], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 0.650677, 'e_o_k': [0.569342, 0.341605], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 1.827166, 'e_o_k': [1.305118, 0.783071, 0.469843], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 88.319984
    return processors, tasks, B_BUDGET
