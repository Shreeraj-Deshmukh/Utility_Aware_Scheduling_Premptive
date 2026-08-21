"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320011, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320011, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.419192, 'e_o_k': [1.103816, 0.883053], 'p_i': 10, 'u_i': 1.9248},
        {'id': 1, 'e_m': 0.272690, 'e_o_k': [0.103480, 0.082784, 0.066227, 0.052982, 0.042385, 0.033908], 'p_i': 20, 'u_i': 3.6832},
        {'id': 2, 'e_m': 0.719531, 'e_o_k': [0.341241, 0.272993, 0.218394, 0.174715], 'p_i': 40, 'u_i': 2.0214},
        {'id': 3, 'e_m': 14.541944, 'e_o_k': [5.518345, 4.414676, 3.531741, 2.825393, 2.260314, 1.808251], 'p_i': 80, 'u_i': 3.5232},
        {'id': 4, 'e_m': 0.153738, 'e_o_k': [0.119574, 0.095659], 'p_i': 10, 'u_i': 1.0606},
        {'id': 5, 'e_m': 2.344799, 'e_o_k': [1.112032, 0.889626, 0.711701, 0.569360], 'p_i': 80, 'u_i': 3.4010},
    ]
    B_BUDGET = 88.320011
    return processors, tasks, B_BUDGET
