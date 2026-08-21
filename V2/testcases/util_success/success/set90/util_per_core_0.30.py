"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.641943, 'e_o_k': [0.057289, 0.045831, 0.036665, 0.029332, 0.023466], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 1.546684, 'e_o_k': [0.125771, 0.100617, 0.080494, 0.064395, 0.051516, 0.041213], 'p_i': 20, 'u_i': 3.3367},
        {'id': 2, 'e_m': 1.347184, 'e_o_k': [0.165637, 0.132510, 0.106008], 'p_i': 40, 'u_i': 4.5472},
        {'id': 3, 'e_m': 0.546821, 'e_o_k': [0.055571, 0.044457, 0.035566, 0.028452], 'p_i': 80, 'u_i': 1.6834},
        {'id': 4, 'e_m': 1.666273, 'e_o_k': [0.277712, 0.222170], 'p_i': 40, 'u_i': 3.8684},
        {'id': 5, 'e_m': 10.444300, 'e_o_k': [1.740717, 1.392573], 'p_i': 40, 'u_i': 4.7513},
        {'id': 6, 'e_m': 4.463145, 'e_o_k': [0.362928, 0.290343, 0.232274, 0.185819, 0.148655, 0.118924], 'p_i': 40, 'u_i': 2.4512},
        {'id': 7, 'e_m': 0.036136, 'e_o_k': [0.006023, 0.004818], 'p_i': 10, 'u_i': 1.4858},
    ]
    B_BUDGET = 71.759994
    return processors, tasks, B_BUDGET
