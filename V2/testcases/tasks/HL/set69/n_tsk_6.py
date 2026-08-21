"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.080666, 'e_o_k': [0.010933, 0.008746, 0.006997, 0.005597, 0.004478, 0.003582], 'p_i': 10, 'u_i': 1.7448},
        {'id': 1, 'e_m': 1.254278, 'e_o_k': [0.186560, 0.149248, 0.119398, 0.095519, 0.076415], 'p_i': 20, 'u_i': 2.9486},
        {'id': 2, 'e_m': 1.191263, 'e_o_k': [0.177187, 0.141749, 0.113400, 0.090720, 0.072576], 'p_i': 40, 'u_i': 1.5908},
        {'id': 3, 'e_m': 12.891421, 'e_o_k': [1.917453, 1.533963, 1.227170, 0.981736, 0.785389], 'p_i': 80, 'u_i': 1.2188},
        {'id': 4, 'e_m': 2.735946, 'e_o_k': [0.560645, 0.448516, 0.358813], 'p_i': 10, 'u_i': 2.5958},
        {'id': 5, 'e_m': 2.647005, 'e_o_k': [0.542419, 0.433935, 0.347148], 'p_i': 10, 'u_i': 3.0557},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
