"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.51999, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.51999, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.892187, 'e_o_k': [0.497173, 0.397739, 0.318191, 0.254553], 'p_i': 10, 'u_i': 2.1780},
        {'id': 1, 'e_m': 1.663339, 'e_o_k': [0.204509, 0.163607, 0.130886], 'p_i': 20, 'u_i': 3.8388},
        {'id': 2, 'e_m': 4.331784, 'e_o_k': [0.440222, 0.352178, 0.281742, 0.225394], 'p_i': 40, 'u_i': 1.0041},
        {'id': 3, 'e_m': 11.747903, 'e_o_k': [1.957984, 1.566387], 'p_i': 80, 'u_i': 4.1994},
        {'id': 4, 'e_m': 2.501011, 'e_o_k': [0.203374, 0.162699, 0.130159, 0.104127, 0.083302, 0.066642], 'p_i': 40, 'u_i': 2.8402},
        {'id': 5, 'e_m': 1.102472, 'e_o_k': [0.089649, 0.071720, 0.057376, 0.045900, 0.036720, 0.029376], 'p_i': 10, 'u_i': 1.6917},
        {'id': 6, 'e_m': 0.555759, 'e_o_k': [0.049598, 0.039678, 0.031743, 0.025394, 0.020315], 'p_i': 10, 'u_i': 1.6028},
        {'id': 7, 'e_m': 11.529801, 'e_o_k': [1.417598, 1.134079, 0.907263], 'p_i': 80, 'u_i': 2.5090},
    ]
    B_BUDGET = 143.519990
    return processors, tasks, B_BUDGET
