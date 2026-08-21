"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520016, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520016, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.139591, 'e_o_k': [0.115812, 0.092650, 0.074120, 0.059296], 'p_i': 10, 'u_i': 3.3255},
        {'id': 1, 'e_m': 3.400852, 'e_o_k': [0.276546, 0.221237, 0.176989, 0.141592, 0.113273, 0.090619], 'p_i': 20, 'u_i': 3.8694},
        {'id': 2, 'e_m': 2.310270, 'e_o_k': [0.385045, 0.308036], 'p_i': 40, 'u_i': 3.5739},
        {'id': 3, 'e_m': 12.527562, 'e_o_k': [1.018700, 0.814960, 0.651968, 0.521574, 0.417259, 0.333808], 'p_i': 80, 'u_i': 3.1864},
        {'id': 4, 'e_m': 13.010683, 'e_o_k': [1.322224, 1.057779, 0.846223, 0.676979], 'p_i': 80, 'u_i': 1.9174},
        {'id': 5, 'e_m': 36.177962, 'e_o_k': [2.941872, 2.353497, 1.882798, 1.506238, 1.204991, 0.963993], 'p_i': 80, 'u_i': 3.2100},
        {'id': 6, 'e_m': 0.577233, 'e_o_k': [0.070971, 0.056777, 0.045422], 'p_i': 10, 'u_i': 2.5681},
        {'id': 7, 'e_m': 1.162629, 'e_o_k': [0.193771, 0.155017], 'p_i': 40, 'u_i': 3.1630},
    ]
    B_BUDGET = 143.520016
    return processors, tasks, B_BUDGET
