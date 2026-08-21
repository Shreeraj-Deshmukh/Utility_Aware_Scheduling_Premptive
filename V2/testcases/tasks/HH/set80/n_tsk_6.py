"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.356968, 'e_o_k': [0.169294, 0.135435, 0.108348, 0.086678], 'p_i': 10, 'u_i': 4.6156},
        {'id': 1, 'e_m': 0.792605, 'e_o_k': [0.375897, 0.300717, 0.240574, 0.192459], 'p_i': 20, 'u_i': 1.3815},
        {'id': 2, 'e_m': 1.215817, 'e_o_k': [0.697600, 0.558080, 0.446464], 'p_i': 40, 'u_i': 2.2542},
        {'id': 3, 'e_m': 26.585889, 'e_o_k': [10.088756, 8.071005, 6.456804, 5.165443, 4.132354, 3.305883], 'p_i': 80, 'u_i': 3.1493},
        {'id': 4, 'e_m': 6.230606, 'e_o_k': [2.954894, 2.363916, 1.891132, 1.512906], 'p_i': 20, 'u_i': 4.3022},
        {'id': 5, 'e_m': 4.033887, 'e_o_k': [1.530771, 1.224617, 0.979693, 0.783755, 0.627004, 0.501603], 'p_i': 80, 'u_i': 4.8493},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
