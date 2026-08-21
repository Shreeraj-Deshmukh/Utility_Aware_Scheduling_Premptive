"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.404244, 'e_o_k': [0.068470, 0.054776, 0.043821, 0.035056], 'p_i': 10, 'u_i': 3.9662},
        {'id': 1, 'e_m': 1.599701, 'e_o_k': [0.327808, 0.262246, 0.209797], 'p_i': 20, 'u_i': 1.8989},
        {'id': 2, 'e_m': 11.040808, 'e_o_k': [3.066891, 2.453513], 'p_i': 40, 'u_i': 3.5356},
        {'id': 3, 'e_m': 32.285624, 'e_o_k': [4.375600, 3.500480, 2.800384, 2.240307, 1.792246, 1.433796], 'p_i': 80, 'u_i': 1.2138},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
