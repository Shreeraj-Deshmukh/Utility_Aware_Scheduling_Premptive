"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.842522, 'e_o_k': [0.789589, 0.631671], 'p_i': 10, 'u_i': 2.1906},
        {'id': 1, 'e_m': 6.188268, 'e_o_k': [0.920435, 0.736348, 0.589078, 0.471263, 0.377010], 'p_i': 20, 'u_i': 4.5509},
        {'id': 2, 'e_m': 0.200736, 'e_o_k': [0.029857, 0.023886, 0.019109, 0.015287, 0.012230], 'p_i': 40, 'u_i': 2.6037},
        {'id': 3, 'e_m': 16.105285, 'e_o_k': [4.473690, 3.578952], 'p_i': 80, 'u_i': 2.6419},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
