"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.101224, 'e_o_k': [0.015056, 0.012045, 0.009636, 0.007709, 0.006167], 'p_i': 10, 'u_i': 1.6984},
        {'id': 1, 'e_m': 1.684546, 'e_o_k': [0.285323, 0.228258, 0.182607, 0.146085], 'p_i': 20, 'u_i': 3.4597},
        {'id': 2, 'e_m': 14.212239, 'e_o_k': [2.407222, 1.925778, 1.540622, 1.232498], 'p_i': 40, 'u_i': 4.7133},
        {'id': 3, 'e_m': 18.089584, 'e_o_k': [2.451642, 1.961313, 1.569051, 1.255240, 1.004192, 0.803354], 'p_i': 80, 'u_i': 2.1441},
        {'id': 4, 'e_m': 2.706115, 'e_o_k': [0.402504, 0.322003, 0.257603, 0.206082, 0.164866], 'p_i': 40, 'u_i': 1.5180},
        {'id': 5, 'e_m': 0.565717, 'e_o_k': [0.095819, 0.076655, 0.061324, 0.049059], 'p_i': 10, 'u_i': 2.4726},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
