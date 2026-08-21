"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.920347, 'e_o_k': [2.271381, 1.817105], 'p_i': 10, 'u_i': 1.9752},
        {'id': 1, 'e_m': 0.834414, 'e_o_k': [0.648988, 0.519191], 'p_i': 20, 'u_i': 3.9662},
        {'id': 2, 'e_m': 4.634773, 'e_o_k': [3.604823, 2.883859], 'p_i': 40, 'u_i': 1.9890},
        {'id': 3, 'e_m': 0.634609, 'e_o_k': [0.493585, 0.394868], 'p_i': 80, 'u_i': 3.3639},
        {'id': 4, 'e_m': 3.457185, 'e_o_k': [2.688922, 2.151138], 'p_i': 40, 'u_i': 4.7869},
        {'id': 5, 'e_m': 0.421109, 'e_o_k': [0.327529, 0.262023], 'p_i': 10, 'u_i': 2.7944},
        {'id': 6, 'e_m': 0.414008, 'e_o_k': [0.322006, 0.257605], 'p_i': 10, 'u_i': 4.7769},
        {'id': 7, 'e_m': 1.725014, 'e_o_k': [1.341677, 1.073342], 'p_i': 10, 'u_i': 1.3167},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
