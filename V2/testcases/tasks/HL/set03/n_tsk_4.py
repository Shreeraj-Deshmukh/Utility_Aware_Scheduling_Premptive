"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.661670, 'e_o_k': [0.247155, 0.197724, 0.158179, 0.126543, 0.101235], 'p_i': 10, 'u_i': 3.1570},
        {'id': 1, 'e_m': 5.070765, 'e_o_k': [0.754219, 0.603375, 0.482700, 0.386160, 0.308928], 'p_i': 20, 'u_i': 1.1037},
        {'id': 2, 'e_m': 4.227938, 'e_o_k': [0.716114, 0.572891, 0.458313, 0.366650], 'p_i': 40, 'u_i': 1.2642},
        {'id': 3, 'e_m': 21.967705, 'e_o_k': [2.977235, 2.381788, 1.905430, 1.524344, 1.219475, 0.975580], 'p_i': 80, 'u_i': 2.8053},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
