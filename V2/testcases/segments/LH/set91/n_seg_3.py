"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.543832, 'e_o_k': [0.312035, 0.249628, 0.199702], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.195966, 'e_o_k': [0.112439, 0.089951, 0.071961], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 6.548072, 'e_o_k': [3.757091, 3.005672, 2.404538], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 3.827555, 'e_o_k': [2.196138, 1.756911, 1.405528], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.151912, 'e_o_k': [0.087162, 0.069730, 0.055784], 'p_i': 20, 'u_i': 4.2274},
        {'id': 5, 'e_m': 0.377358, 'e_o_k': [0.216517, 0.173214, 0.138571], 'p_i': 20, 'u_i': 3.9205},
        {'id': 6, 'e_m': 2.516575, 'e_o_k': [1.443937, 1.155149, 0.924120], 'p_i': 40, 'u_i': 1.6340},
        {'id': 7, 'e_m': 1.395776, 'e_o_k': [0.800855, 0.640684, 0.512547], 'p_i': 40, 'u_i': 3.9145},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
