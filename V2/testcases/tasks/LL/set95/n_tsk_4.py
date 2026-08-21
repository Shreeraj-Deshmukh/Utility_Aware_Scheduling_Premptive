"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.609466, 'e_o_k': [0.218127, 0.174502, 0.139601, 0.111681, 0.089345, 0.071476], 'p_i': 10, 'u_i': 2.6491},
        {'id': 1, 'e_m': 2.570899, 'e_o_k': [0.526824, 0.421459, 0.337167], 'p_i': 20, 'u_i': 3.0546},
        {'id': 2, 'e_m': 3.882674, 'e_o_k': [0.577504, 0.462003, 0.369602, 0.295682, 0.236546], 'p_i': 40, 'u_i': 3.4882},
        {'id': 3, 'e_m': 1.075331, 'e_o_k': [0.159943, 0.127955, 0.102364, 0.081891, 0.065513], 'p_i': 80, 'u_i': 2.0277},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
