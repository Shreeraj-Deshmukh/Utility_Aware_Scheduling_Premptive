"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.972467, 'e_o_k': [0.164713, 0.131771, 0.105416, 0.084333], 'p_i': 10, 'u_i': 2.8432},
        {'id': 1, 'e_m': 3.104081, 'e_o_k': [0.636082, 0.508866, 0.407093], 'p_i': 20, 'u_i': 4.5844},
        {'id': 2, 'e_m': 1.034213, 'e_o_k': [0.287281, 0.229825], 'p_i': 40, 'u_i': 1.8342},
        {'id': 3, 'e_m': 2.973567, 'e_o_k': [0.609337, 0.487470, 0.389976], 'p_i': 80, 'u_i': 2.1428},
        {'id': 4, 'e_m': 0.732465, 'e_o_k': [0.124062, 0.099250, 0.079400, 0.063520], 'p_i': 10, 'u_i': 3.7337},
        {'id': 5, 'e_m': 0.451117, 'e_o_k': [0.067099, 0.053679, 0.042943, 0.034354, 0.027484], 'p_i': 40, 'u_i': 3.4112},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
