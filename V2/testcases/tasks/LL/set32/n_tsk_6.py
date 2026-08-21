"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.692176, 'e_o_k': [0.117239, 0.093791, 0.075033, 0.060026], 'p_i': 10, 'u_i': 1.0669},
        {'id': 1, 'e_m': 0.927432, 'e_o_k': [0.157085, 0.125668, 0.100535, 0.080428], 'p_i': 20, 'u_i': 2.5210},
        {'id': 2, 'e_m': 0.897482, 'e_o_k': [0.183910, 0.147128, 0.117703], 'p_i': 40, 'u_i': 3.1907},
        {'id': 3, 'e_m': 8.776195, 'e_o_k': [1.486483, 1.189186, 0.951349, 0.761079], 'p_i': 80, 'u_i': 4.8710},
        {'id': 4, 'e_m': 1.647999, 'e_o_k': [0.457778, 0.366222], 'p_i': 20, 'u_i': 3.8865},
        {'id': 5, 'e_m': 0.698713, 'e_o_k': [0.194087, 0.155270], 'p_i': 10, 'u_i': 3.2848},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
