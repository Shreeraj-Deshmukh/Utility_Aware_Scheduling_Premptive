"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400014, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400014, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.178357, 'e_o_k': [0.026529, 0.021223, 0.016978, 0.013583, 0.010866], 'p_i': 10, 'u_i': 3.3453},
        {'id': 1, 'e_m': 6.375379, 'e_o_k': [1.306430, 1.045144, 0.836115], 'p_i': 20, 'u_i': 2.8841},
        {'id': 2, 'e_m': 1.100311, 'e_o_k': [0.225474, 0.180379, 0.144303], 'p_i': 40, 'u_i': 2.2513},
        {'id': 3, 'e_m': 13.676876, 'e_o_k': [2.316544, 1.853235, 1.482588, 1.186071], 'p_i': 80, 'u_i': 1.5109},
        {'id': 4, 'e_m': 2.125189, 'e_o_k': [0.435490, 0.348392, 0.278713], 'p_i': 10, 'u_i': 1.6396},
        {'id': 5, 'e_m': 1.048155, 'e_o_k': [0.214786, 0.171829, 0.137463], 'p_i': 20, 'u_i': 4.1445},
    ]
    B_BUDGET = 110.400014
    return processors, tasks, B_BUDGET
