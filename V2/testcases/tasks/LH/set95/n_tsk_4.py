"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.609466, 'e_o_k': [0.610757, 0.488605, 0.390884, 0.312707, 0.250166, 0.200133], 'p_i': 10, 'u_i': 2.6491},
        {'id': 1, 'e_m': 2.570899, 'e_o_k': [1.475106, 1.180085, 0.944068], 'p_i': 20, 'u_i': 3.0546},
        {'id': 2, 'e_m': 3.882674, 'e_o_k': [1.617011, 1.293609, 1.034887, 0.827910, 0.662328], 'p_i': 40, 'u_i': 3.4882},
        {'id': 3, 'e_m': 1.075331, 'e_o_k': [0.447841, 0.358273, 0.286618, 0.229295, 0.183436], 'p_i': 80, 'u_i': 2.0277},
    ]
    B_BUDGET = 88.320009
    return processors, tasks, B_BUDGET
