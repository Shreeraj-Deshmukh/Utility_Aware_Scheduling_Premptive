"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319982, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319982, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.056307, 'e_o_k': [0.026277, 0.026277, 0.026277], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 0.343444, 'e_o_k': [0.240411, 0.240411], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 1.086388, 'e_o_k': [0.760472, 0.760472], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 2.157450, 'e_o_k': [0.755108, 0.755108, 0.755108, 0.755108], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.190372, 'e_o_k': [0.066630, 0.066630, 0.066630, 0.066630], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 4.007311, 'e_o_k': [1.870078, 1.870078, 1.870078], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 1.096980, 'e_o_k': [0.383943, 0.383943, 0.383943, 0.383943], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 11.539405, 'e_o_k': [5.385056, 5.385056, 5.385056], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 88.319982
    return processors, tasks, B_BUDGET
