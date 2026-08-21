"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100744, 'e_o_k': [0.057804, 0.046243, 0.036995], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 0.720915, 'e_o_k': [0.413640, 0.330912, 0.264729], 'p_i': 20, 'u_i': 1.1969},
        {'id': 2, 'e_m': 4.330945, 'e_o_k': [2.484969, 1.987975, 1.590380], 'p_i': 40, 'u_i': 4.6056},
        {'id': 3, 'e_m': 4.451086, 'e_o_k': [2.553902, 2.043122, 1.634497], 'p_i': 80, 'u_i': 2.0280},
        {'id': 4, 'e_m': 2.996813, 'e_o_k': [1.719483, 1.375586, 1.100469], 'p_i': 40, 'u_i': 3.8591},
        {'id': 5, 'e_m': 2.171206, 'e_o_k': [1.245774, 0.996619, 0.797295], 'p_i': 80, 'u_i': 4.1547},
        {'id': 6, 'e_m': 0.650677, 'e_o_k': [0.373339, 0.298671, 0.238937], 'p_i': 10, 'u_i': 4.9057},
        {'id': 7, 'e_m': 1.827166, 'e_o_k': [1.048374, 0.838699, 0.670959], 'p_i': 80, 'u_i': 4.2009},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
