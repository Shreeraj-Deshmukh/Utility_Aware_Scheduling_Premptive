"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.067880, 'e_o_k': [0.423746, 0.338997, 0.271197], 'p_i': 10, 'u_i': 2.1828},
        {'id': 1, 'e_m': 1.237267, 'e_o_k': [0.253538, 0.202831, 0.162264], 'p_i': 20, 'u_i': 3.4051},
        {'id': 2, 'e_m': 3.123831, 'e_o_k': [0.529104, 0.423283, 0.338627, 0.270901], 'p_i': 40, 'u_i': 2.6596},
        {'id': 3, 'e_m': 4.260232, 'e_o_k': [0.577380, 0.461904, 0.369523, 0.295619, 0.236495, 0.189196], 'p_i': 80, 'u_i': 2.1030},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
