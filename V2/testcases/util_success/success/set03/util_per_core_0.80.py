"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360018, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360018, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.611869, 'e_o_k': [0.198181, 0.158545, 0.126836], 'p_i': 10, 'u_i': 3.7384},
        {'id': 1, 'e_m': 3.573447, 'e_o_k': [0.290581, 0.232465, 0.185972, 0.148777, 0.119022, 0.095218], 'p_i': 20, 'u_i': 1.0034},
        {'id': 2, 'e_m': 19.412410, 'e_o_k': [1.732426, 1.385941, 1.108753, 0.887002, 0.709602], 'p_i': 40, 'u_i': 2.3713},
        {'id': 3, 'e_m': 16.299949, 'e_o_k': [1.325458, 1.060366, 0.848293, 0.678634, 0.542908, 0.434326], 'p_i': 80, 'u_i': 1.9623},
        {'id': 4, 'e_m': 1.730284, 'e_o_k': [0.154416, 0.123533, 0.098826, 0.079061, 0.063249], 'p_i': 10, 'u_i': 1.2428},
        {'id': 5, 'e_m': 0.399746, 'e_o_k': [0.035675, 0.028540, 0.022832, 0.018265, 0.014612], 'p_i': 20, 'u_i': 4.6455},
        {'id': 6, 'e_m': 1.068612, 'e_o_k': [0.108599, 0.086879, 0.069503, 0.055603], 'p_i': 10, 'u_i': 2.5101},
        {'id': 7, 'e_m': 10.848169, 'e_o_k': [1.333791, 1.067033, 0.853626], 'p_i': 40, 'u_i': 1.7945},
    ]
    B_BUDGET = 191.360018
    return processors, tasks, B_BUDGET
