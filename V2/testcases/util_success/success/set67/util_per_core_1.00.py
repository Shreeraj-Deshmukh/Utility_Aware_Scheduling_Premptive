"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199999, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199999, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.642925, 'e_o_k': [0.235863, 0.188690, 0.150952, 0.120762, 0.096610], 'p_i': 10, 'u_i': 1.8232},
        {'id': 1, 'e_m': 4.195754, 'e_o_k': [0.374443, 0.299554, 0.239643, 0.191715, 0.153372], 'p_i': 20, 'u_i': 4.2323},
        {'id': 2, 'e_m': 13.344001, 'e_o_k': [1.190862, 0.952689, 0.762151, 0.609721, 0.487777], 'p_i': 40, 'u_i': 3.7021},
        {'id': 3, 'e_m': 11.164676, 'e_o_k': [1.372706, 1.098165, 0.878532], 'p_i': 80, 'u_i': 1.4717},
        {'id': 4, 'e_m': 2.983442, 'e_o_k': [0.366817, 0.293453, 0.234763], 'p_i': 10, 'u_i': 2.9634},
        {'id': 5, 'e_m': 12.498658, 'e_o_k': [1.115420, 0.892336, 0.713869, 0.571095, 0.456876], 'p_i': 80, 'u_i': 1.6416},
        {'id': 6, 'e_m': 5.018715, 'e_o_k': [0.447886, 0.358309, 0.286647, 0.229318, 0.183454], 'p_i': 20, 'u_i': 4.1520},
        {'id': 7, 'e_m': 3.472482, 'e_o_k': [0.352894, 0.282316, 0.225852, 0.180682], 'p_i': 10, 'u_i': 2.8128},
    ]
    B_BUDGET = 239.199999
    return processors, tasks, B_BUDGET
