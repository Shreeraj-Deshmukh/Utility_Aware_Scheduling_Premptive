"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.072203, 'e_o_k': [0.041428, 0.033142, 0.026514], 'p_i': 10, 'u_i': 4.0506},
        {'id': 1, 'e_m': 3.542872, 'e_o_k': [2.032795, 1.626236, 1.300989], 'p_i': 20, 'u_i': 2.8657},
        {'id': 2, 'e_m': 5.455722, 'e_o_k': [2.587402, 2.069921, 1.655937, 1.324750], 'p_i': 40, 'u_i': 2.1758},
        {'id': 3, 'e_m': 6.580644, 'e_o_k': [5.118279, 4.094623], 'p_i': 80, 'u_i': 2.5351},
        {'id': 4, 'e_m': 1.686436, 'e_o_k': [0.799800, 0.639840, 0.511872, 0.409498], 'p_i': 40, 'u_i': 3.6072},
        {'id': 5, 'e_m': 14.192964, 'e_o_k': [5.385915, 4.308732, 3.446986, 2.757589, 2.206071, 1.764857], 'p_i': 40, 'u_i': 4.5999},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
