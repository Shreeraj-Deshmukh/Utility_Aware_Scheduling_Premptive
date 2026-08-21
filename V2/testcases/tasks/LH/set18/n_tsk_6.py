"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.679884, 'e_o_k': [0.390097, 0.312078, 0.249662], 'p_i': 10, 'u_i': 4.6061},
        {'id': 1, 'e_m': 0.417910, 'e_o_k': [0.174046, 0.139237, 0.111390, 0.089112, 0.071289], 'p_i': 20, 'u_i': 1.8658},
        {'id': 2, 'e_m': 1.347507, 'e_o_k': [1.048061, 0.838449], 'p_i': 40, 'u_i': 4.6317},
        {'id': 3, 'e_m': 3.937087, 'e_o_k': [1.639672, 1.311738, 1.049390, 0.839512, 0.671610], 'p_i': 80, 'u_i': 4.1058},
        {'id': 4, 'e_m': 1.950051, 'e_o_k': [1.118882, 0.895105, 0.716084], 'p_i': 40, 'u_i': 1.5782},
        {'id': 5, 'e_m': 3.589272, 'e_o_k': [1.494818, 1.195854, 0.956684, 0.765347, 0.612277], 'p_i': 20, 'u_i': 1.2072},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
