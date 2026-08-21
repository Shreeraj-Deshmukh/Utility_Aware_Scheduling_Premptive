"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.218931, 'e_o_k': [1.221513, 0.977210, 0.781768, 0.625415, 0.500332, 0.400265], 'p_i': 10, 'u_i': 2.6491},
        {'id': 1, 'e_m': 5.141798, 'e_o_k': [2.950212, 2.360170, 1.888136], 'p_i': 20, 'u_i': 3.0546},
        {'id': 2, 'e_m': 7.765348, 'e_o_k': [3.234022, 2.587217, 2.069774, 1.655819, 1.324655], 'p_i': 40, 'u_i': 3.4882},
        {'id': 3, 'e_m': 2.150661, 'e_o_k': [0.895682, 0.716546, 0.573237, 0.458589, 0.366871], 'p_i': 80, 'u_i': 2.0277},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
