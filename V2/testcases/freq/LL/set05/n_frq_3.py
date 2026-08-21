"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 30, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "freq", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 30, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "freq", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.394847, 'e_o_k': [0.066878, 0.053502, 0.042802, 0.034241], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.122647, 'e_o_k': [0.034069, 0.027255], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 1.655397, 'e_o_k': [0.224352, 0.179482, 0.143586, 0.114868, 0.091895, 0.073516], 'p_i': 40, 'u_i': 4.1771},
        {'id': 3, 'e_m': 0.814260, 'e_o_k': [0.137917, 0.110333, 0.088267, 0.070613], 'p_i': 80, 'u_i': 4.0903},
        {'id': 4, 'e_m': 1.025576, 'e_o_k': [0.173709, 0.138967, 0.111174, 0.088939], 'p_i': 20, 'u_i': 2.9627},
        {'id': 5, 'e_m': 0.055175, 'e_o_k': [0.009345, 0.007476, 0.005981, 0.004785], 'p_i': 80, 'u_i': 1.9286},
        {'id': 6, 'e_m': 1.611854, 'e_o_k': [0.273010, 0.218408, 0.174727, 0.139781], 'p_i': 10, 'u_i': 3.5955},
        {'id': 7, 'e_m': 3.586638, 'e_o_k': [0.533472, 0.426777, 0.341422, 0.273138, 0.218510], 'p_i': 40, 'u_i': 1.8182},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
