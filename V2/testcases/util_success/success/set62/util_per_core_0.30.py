"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760002, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760002, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.588877, 'e_o_k': [0.129202, 0.103362, 0.082689, 0.066152, 0.052921, 0.042337], 'p_i': 10, 'u_i': 2.4480},
        {'id': 1, 'e_m': 1.405876, 'e_o_k': [0.114321, 0.091457, 0.073166, 0.058532, 0.046826, 0.037461], 'p_i': 20, 'u_i': 3.0914},
        {'id': 2, 'e_m': 0.964972, 'e_o_k': [0.098066, 0.078453, 0.062762, 0.050210], 'p_i': 40, 'u_i': 2.6989},
        {'id': 3, 'e_m': 1.284706, 'e_o_k': [0.214118, 0.171294], 'p_i': 80, 'u_i': 4.1647},
        {'id': 4, 'e_m': 2.180752, 'e_o_k': [0.221621, 0.177297, 0.141838, 0.113470], 'p_i': 10, 'u_i': 1.2796},
        {'id': 5, 'e_m': 0.363048, 'e_o_k': [0.036895, 0.029516, 0.023613, 0.018890], 'p_i': 10, 'u_i': 2.4526},
        {'id': 6, 'e_m': 5.673377, 'e_o_k': [0.697546, 0.558037, 0.446430], 'p_i': 80, 'u_i': 3.7482},
        {'id': 7, 'e_m': 0.213527, 'e_o_k': [0.019056, 0.015245, 0.012196, 0.009757, 0.007805], 'p_i': 40, 'u_i': 2.1247},
    ]
    B_BUDGET = 71.760002
    return processors, tasks, B_BUDGET
