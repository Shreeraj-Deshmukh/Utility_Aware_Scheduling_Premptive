"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.600658, 'e_o_k': [0.918410, 0.734728, 0.587783], 'p_i': 10, 'u_i': 1.6704},
        {'id': 1, 'e_m': 1.481795, 'e_o_k': [0.617121, 0.493697, 0.394957, 0.315966, 0.252773], 'p_i': 20, 'u_i': 3.6515},
        {'id': 2, 'e_m': 1.500331, 'e_o_k': [0.711539, 0.569231, 0.455385, 0.364308], 'p_i': 40, 'u_i': 1.3011},
        {'id': 3, 'e_m': 10.266896, 'e_o_k': [4.869124, 3.895299, 3.116239, 2.492991], 'p_i': 80, 'u_i': 4.8603},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
