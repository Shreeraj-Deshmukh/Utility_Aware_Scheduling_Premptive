"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.963605, 'e_o_k': [0.501966, 0.401573, 0.321258, 0.257006], 'p_i': 10, 'u_i': 2.9572},
        {'id': 1, 'e_m': 4.069868, 'e_o_k': [0.689341, 0.551473, 0.441178, 0.352942], 'p_i': 20, 'u_i': 4.0373},
        {'id': 2, 'e_m': 0.778980, 'e_o_k': [0.115864, 0.092692, 0.074153, 0.059323, 0.047458], 'p_i': 40, 'u_i': 2.8937},
        {'id': 3, 'e_m': 22.453726, 'e_o_k': [3.803138, 3.042510, 2.434008, 1.947207], 'p_i': 80, 'u_i': 3.5048},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
