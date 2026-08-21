"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400014, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400014, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.083295, 'e_o_k': [0.146817, 0.117453, 0.093963, 0.075170, 0.060136, 0.048109], 'p_i': 10, 'u_i': 3.6469},
        {'id': 1, 'e_m': 0.351454, 'e_o_k': [0.052275, 0.041820, 0.033456, 0.026765, 0.021412], 'p_i': 20, 'u_i': 1.4903},
        {'id': 2, 'e_m': 5.041036, 'e_o_k': [0.853834, 0.683067, 0.546454, 0.437163], 'p_i': 40, 'u_i': 2.4704},
        {'id': 3, 'e_m': 2.805236, 'e_o_k': [0.574843, 0.459875, 0.367900], 'p_i': 80, 'u_i': 4.2349},
        {'id': 4, 'e_m': 8.758930, 'e_o_k': [1.187079, 0.949663, 0.759730, 0.607784, 0.486227, 0.388982], 'p_i': 40, 'u_i': 4.1771},
        {'id': 5, 'e_m': 11.761329, 'e_o_k': [1.992095, 1.593676, 1.274941, 1.019953], 'p_i': 40, 'u_i': 4.0903},
    ]
    B_BUDGET = 110.400014
    return processors, tasks, B_BUDGET
