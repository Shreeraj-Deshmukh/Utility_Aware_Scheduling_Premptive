"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.231133, 'e_o_k': [0.109616, 0.087693, 0.070154, 0.056123], 'p_i': 10, 'u_i': 4.2108},
        {'id': 1, 'e_m': 1.903134, 'e_o_k': [1.091962, 0.873570, 0.698856], 'p_i': 20, 'u_i': 3.3354},
        {'id': 2, 'e_m': 9.454475, 'e_o_k': [4.483829, 3.587064, 2.869651, 2.295721], 'p_i': 40, 'u_i': 1.0371},
        {'id': 3, 'e_m': 3.629449, 'e_o_k': [1.511551, 1.209241, 0.967392, 0.773914, 0.619131], 'p_i': 80, 'u_i': 1.4152},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
