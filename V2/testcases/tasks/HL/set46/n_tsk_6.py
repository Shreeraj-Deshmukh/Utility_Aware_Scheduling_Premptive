"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.147430, 'e_o_k': [0.318730, 0.254984], 'p_i': 10, 'u_i': 2.0200},
        {'id': 1, 'e_m': 0.711598, 'e_o_k': [0.145819, 0.116655, 0.093324], 'p_i': 20, 'u_i': 3.9687},
        {'id': 2, 'e_m': 14.390903, 'e_o_k': [1.950367, 1.560294, 1.248235, 0.998588, 0.798871, 0.639096], 'p_i': 40, 'u_i': 2.3030},
        {'id': 3, 'e_m': 9.199953, 'e_o_k': [1.885236, 1.508189, 1.206551], 'p_i': 80, 'u_i': 2.6501},
        {'id': 4, 'e_m': 1.420179, 'e_o_k': [0.211236, 0.168989, 0.135191, 0.108153, 0.086522], 'p_i': 10, 'u_i': 1.7748},
        {'id': 5, 'e_m': 0.657744, 'e_o_k': [0.134784, 0.107827, 0.086262], 'p_i': 20, 'u_i': 3.9815},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
