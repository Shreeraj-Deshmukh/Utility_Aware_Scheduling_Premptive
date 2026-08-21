"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.36, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.36, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.371825, 'e_o_k': [0.139413, 0.111531, 0.089224, 0.071380], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 4.968818, 'e_o_k': [0.504961, 0.403969, 0.323175, 0.258540], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.096142, 'e_o_k': [0.008580, 0.006864, 0.005491, 0.004393, 0.003514], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 22.642694, 'e_o_k': [2.301087, 1.840869, 1.472696, 1.178156], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 19.725959, 'e_o_k': [3.287660, 2.630128], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 6.414326, 'e_o_k': [0.572435, 0.457948, 0.366358, 0.293087, 0.234469], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 19.214107, 'e_o_k': [1.714729, 1.371783, 1.097426, 0.877941, 0.702353], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 2.820474, 'e_o_k': [0.286633, 0.229307, 0.183445, 0.146756], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 191.360000
    return processors, tasks, B_BUDGET
