"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360008, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360008, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.423204, 'e_o_k': [0.237201, 0.189760], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 3.912077, 'e_o_k': [0.318117, 0.254494, 0.203595, 0.162876, 0.130301, 0.104241], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 13.157816, 'e_o_k': [1.617764, 1.294211, 1.035369], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 29.796624, 'e_o_k': [3.663519, 2.930815, 2.344652], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 9.638204, 'e_o_k': [0.979492, 0.783594, 0.626875, 0.501500], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.918873, 'e_o_k': [0.074720, 0.059776, 0.047821, 0.038256, 0.030605, 0.024484], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 2.639324, 'e_o_k': [0.235542, 0.188433, 0.150747, 0.120597, 0.096478], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 4.326831, 'e_o_k': [0.721139, 0.576911], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 191.360008
    return processors, tasks, B_BUDGET
