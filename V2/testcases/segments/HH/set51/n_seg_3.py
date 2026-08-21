"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.831177, 'e_o_k': [1.624446, 1.299556, 1.039645], 'p_i': 10, 'u_i': 2.5682},
        {'id': 1, 'e_m': 3.119051, 'e_o_k': [1.789619, 1.431695, 1.145356], 'p_i': 20, 'u_i': 2.9074},
        {'id': 2, 'e_m': 2.015453, 'e_o_k': [1.156407, 0.925126, 0.740101], 'p_i': 40, 'u_i': 4.2053},
        {'id': 3, 'e_m': 2.684483, 'e_o_k': [1.540277, 1.232222, 0.985777], 'p_i': 80, 'u_i': 2.1233},
        {'id': 4, 'e_m': 8.015706, 'e_o_k': [4.599176, 3.679341, 2.943472], 'p_i': 80, 'u_i': 2.8725},
        {'id': 5, 'e_m': 1.186196, 'e_o_k': [0.680604, 0.544483, 0.435587], 'p_i': 20, 'u_i': 1.8909},
        {'id': 6, 'e_m': 2.133652, 'e_o_k': [1.224227, 0.979381, 0.783505], 'p_i': 20, 'u_i': 4.9900},
        {'id': 7, 'e_m': 0.863896, 'e_o_k': [0.495678, 0.396542, 0.317234], 'p_i': 80, 'u_i': 1.9407},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
