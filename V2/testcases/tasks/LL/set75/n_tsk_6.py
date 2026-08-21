"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.611335, 'e_o_k': [0.103546, 0.082837, 0.066269, 0.053015], 'p_i': 10, 'u_i': 4.4576},
        {'id': 1, 'e_m': 0.001467, 'e_o_k': [0.000408, 0.000326], 'p_i': 20, 'u_i': 1.2102},
        {'id': 2, 'e_m': 8.726195, 'e_o_k': [1.788155, 1.430524, 1.144419], 'p_i': 40, 'u_i': 3.7306},
        {'id': 3, 'e_m': 2.728921, 'e_o_k': [0.559205, 0.447364, 0.357891], 'p_i': 80, 'u_i': 4.1325},
        {'id': 4, 'e_m': 0.509449, 'e_o_k': [0.086289, 0.069031, 0.055225, 0.044180], 'p_i': 20, 'u_i': 2.4718},
        {'id': 5, 'e_m': 2.442173, 'e_o_k': [0.330982, 0.264786, 0.211829, 0.169463, 0.135570, 0.108456], 'p_i': 40, 'u_i': 1.1369},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
