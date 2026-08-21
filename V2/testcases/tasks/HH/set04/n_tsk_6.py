"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640015, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640015, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.270665, 'e_o_k': [0.602619, 0.482095, 0.385676, 0.308541], 'p_i': 10, 'u_i': 3.6021},
        {'id': 1, 'e_m': 0.081121, 'e_o_k': [0.046545, 0.037236, 0.029789], 'p_i': 20, 'u_i': 4.3808},
        {'id': 2, 'e_m': 4.023700, 'e_o_k': [1.908259, 1.526607, 1.221286, 0.977028], 'p_i': 40, 'u_i': 1.2748},
        {'id': 3, 'e_m': 7.615399, 'e_o_k': [4.369491, 3.495593, 2.796474], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 4.647066, 'e_o_k': [2.666349, 2.133080, 1.706464], 'p_i': 20, 'u_i': 3.8582},
        {'id': 5, 'e_m': 4.814784, 'e_o_k': [2.762581, 2.210065, 1.768052], 'p_i': 20, 'u_i': 1.6137},
    ]
    B_BUDGET = 176.640015
    return processors, tasks, B_BUDGET
