"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.232409, 'e_o_k': [0.039365, 0.031492, 0.025193, 0.020155], 'p_i': 10, 'u_i': 4.2389},
        {'id': 1, 'e_m': 1.189114, 'e_o_k': [0.176867, 0.141494, 0.113195, 0.090556, 0.072445], 'p_i': 20, 'u_i': 4.7607},
        {'id': 2, 'e_m': 9.509979, 'e_o_k': [1.610769, 1.288615, 1.030892, 0.824714], 'p_i': 40, 'u_i': 3.2703},
        {'id': 3, 'e_m': 38.364318, 'e_o_k': [7.861541, 6.289232, 5.031386], 'p_i': 80, 'u_i': 4.5676},
    ]
    B_BUDGET = 110.400013
    return processors, tasks, B_BUDGET
