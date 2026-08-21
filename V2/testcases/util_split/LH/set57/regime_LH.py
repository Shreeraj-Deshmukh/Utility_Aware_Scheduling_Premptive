"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 27, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_split", "util_per_core": 0.2, "value": "LH"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 27, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_split", "util_per_core": 0.2, "value": "LH"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100744, 'e_o_k': [0.041957, 0.033565, 0.026852, 0.021482, 0.017185], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 0.720915, 'e_o_k': [0.273571, 0.218857, 0.175086, 0.140068, 0.112055, 0.089644], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 4.330945, 'e_o_k': [3.368513, 2.694810], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 4.451086, 'e_o_k': [3.461956, 2.769565], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 2.996813, 'e_o_k': [2.330854, 1.864683], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 2.171206, 'e_o_k': [0.823925, 0.659140, 0.527312, 0.421849, 0.337480, 0.269984], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 0.650677, 'e_o_k': [0.506082, 0.404866], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 1.827166, 'e_o_k': [1.048374, 0.838699, 0.670959], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
