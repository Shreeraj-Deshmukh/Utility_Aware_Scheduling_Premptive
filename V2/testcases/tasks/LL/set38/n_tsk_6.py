"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.413770, 'e_o_k': [0.392714, 0.314171], 'p_i': 10, 'u_i': 1.1650},
        {'id': 1, 'e_m': 1.499929, 'e_o_k': [0.254053, 0.203242, 0.162594, 0.130075], 'p_i': 20, 'u_i': 2.0635},
        {'id': 2, 'e_m': 3.678693, 'e_o_k': [1.021859, 0.817487], 'p_i': 40, 'u_i': 4.3065},
        {'id': 3, 'e_m': 2.202121, 'e_o_k': [0.298449, 0.238759, 0.191007, 0.152806, 0.122245, 0.097796], 'p_i': 80, 'u_i': 1.2855},
        {'id': 4, 'e_m': 2.780337, 'e_o_k': [0.376813, 0.301450, 0.241160, 0.192928, 0.154343, 0.123474], 'p_i': 80, 'u_i': 4.6522},
        {'id': 5, 'e_m': 0.587570, 'e_o_k': [0.087394, 0.069916, 0.055932, 0.044746, 0.035797], 'p_i': 20, 'u_i': 4.9928},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
