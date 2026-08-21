"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.033694, 'e_o_k': [0.026207, 0.020965], 'p_i': 10, 'u_i': 2.5143},
        {'id': 1, 'e_m': 2.566344, 'e_o_k': [1.068801, 0.855041, 0.684033, 0.547226, 0.437781], 'p_i': 20, 'u_i': 1.6130},
        {'id': 2, 'e_m': 3.774422, 'e_o_k': [2.165652, 1.732522, 1.386017], 'p_i': 40, 'u_i': 1.3758},
        {'id': 3, 'e_m': 0.700248, 'e_o_k': [0.401782, 0.321425, 0.257140], 'p_i': 80, 'u_i': 3.6848},
        {'id': 4, 'e_m': 1.539074, 'e_o_k': [1.197058, 0.957646], 'p_i': 10, 'u_i': 1.6851},
        {'id': 5, 'e_m': 0.225847, 'e_o_k': [0.094058, 0.075246, 0.060197, 0.048158, 0.038526], 'p_i': 20, 'u_i': 1.3700},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
