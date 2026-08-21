"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.202122, 'e_o_k': [0.095857, 0.076686, 0.061349, 0.049079], 'p_i': 10, 'u_i': 3.9662},
        {'id': 1, 'e_m': 0.799851, 'e_o_k': [0.458931, 0.367145, 0.293716], 'p_i': 20, 'u_i': 1.8989},
        {'id': 2, 'e_m': 5.520404, 'e_o_k': [4.293648, 3.434918], 'p_i': 40, 'u_i': 3.5356},
        {'id': 3, 'e_m': 16.142812, 'e_o_k': [6.125839, 4.900672, 3.920537, 3.136430, 2.509144, 2.007315], 'p_i': 80, 'u_i': 1.2138},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
