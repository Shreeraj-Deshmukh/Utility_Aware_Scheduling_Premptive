"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.849593, 'e_o_k': [0.353829, 0.283063, 0.226450, 0.181160, 0.144928], 'p_i': 10, 'u_i': 2.2469},
        {'id': 1, 'e_m': 2.065527, 'e_o_k': [0.860227, 0.688181, 0.550545, 0.440436, 0.352349], 'p_i': 20, 'u_i': 2.3819},
        {'id': 2, 'e_m': 0.036634, 'e_o_k': [0.017374, 0.013899, 0.011119, 0.008895], 'p_i': 40, 'u_i': 2.4700},
        {'id': 3, 'e_m': 16.867879, 'e_o_k': [7.024938, 5.619950, 4.495960, 3.596768, 2.877415], 'p_i': 80, 'u_i': 2.1021},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
