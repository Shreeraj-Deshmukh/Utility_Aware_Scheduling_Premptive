"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640014, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.640014, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.198341, 'e_o_k': [0.855958, 0.513575, 0.308145], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 8.371318, 'e_o_k': [7.324904, 4.394942], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.294500, 'e_o_k': [0.189476, 0.113686, 0.068211, 0.040927], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 2.148895, 'e_o_k': [1.880284, 1.128170], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.418546, 'e_o_k': [0.366227, 0.219736], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.283932, 'e_o_k': [0.202808, 0.121685, 0.073011], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.627393, 'e_o_k': [0.368535, 0.221121, 0.132672, 0.079603, 0.047762, 0.028657], 'p_i': 80, 'u_i': 1.9604},
        {'id': 7, 'e_m': 3.482604, 'e_o_k': [2.240646, 1.344388, 0.806633, 0.483980], 'p_i': 20, 'u_i': 2.4961},
    ]
    B_BUDGET = 176.640014
    return processors, tasks, B_BUDGET
