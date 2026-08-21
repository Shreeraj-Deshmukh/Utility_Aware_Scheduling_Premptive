"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.624601, 'e_o_k': [0.358378, 0.286702, 0.229362], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 0.610894, 'e_o_k': [0.350513, 0.280410, 0.224328], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 3.088315, 'e_o_k': [1.771984, 1.417587, 1.134070], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 4.046818, 'e_o_k': [2.321945, 1.857556, 1.486045], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 0.371042, 'e_o_k': [0.212893, 0.170314, 0.136251], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 3.248721, 'e_o_k': [1.864020, 1.491216, 1.192973], 'p_i': 40, 'u_i': 2.6468},
        {'id': 6, 'e_m': 0.378075, 'e_o_k': [0.216928, 0.173542, 0.138834], 'p_i': 20, 'u_i': 2.0597},
        {'id': 7, 'e_m': 5.584342, 'e_o_k': [3.204131, 2.563305, 2.050644], 'p_i': 80, 'u_i': 3.8347},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
