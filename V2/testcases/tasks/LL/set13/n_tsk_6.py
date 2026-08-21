"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.078607, 'e_o_k': [0.011692, 0.009354, 0.007483, 0.005986, 0.004789], 'p_i': 10, 'u_i': 4.4619},
        {'id': 1, 'e_m': 0.506636, 'e_o_k': [0.140732, 0.112586], 'p_i': 20, 'u_i': 2.5387},
        {'id': 2, 'e_m': 1.718166, 'e_o_k': [0.291017, 0.232814, 0.186251, 0.149001], 'p_i': 40, 'u_i': 1.0056},
        {'id': 3, 'e_m': 3.838346, 'e_o_k': [0.650126, 0.520101, 0.416081, 0.332865], 'p_i': 80, 'u_i': 1.2987},
        {'id': 4, 'e_m': 0.919026, 'e_o_k': [0.136695, 0.109356, 0.087485, 0.069988, 0.055990], 'p_i': 20, 'u_i': 3.5939},
        {'id': 5, 'e_m': 2.299227, 'e_o_k': [0.638674, 0.510939], 'p_i': 10, 'u_i': 1.8409},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
