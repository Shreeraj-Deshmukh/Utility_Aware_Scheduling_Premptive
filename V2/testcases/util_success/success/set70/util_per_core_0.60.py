"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519998, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519998, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.681787, 'e_o_k': [0.280298, 0.224238], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 6.819687, 'e_o_k': [0.554554, 0.443643, 0.354915, 0.283932, 0.227145, 0.181716], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 15.859843, 'e_o_k': [1.949981, 1.559985, 1.247988], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 5.520388, 'e_o_k': [0.920065, 0.736052], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 0.935904, 'e_o_k': [0.076105, 0.060884, 0.048707, 0.038966, 0.031172, 0.024938], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 4.741099, 'e_o_k': [0.423111, 0.338489, 0.270791, 0.216633, 0.173306], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 7.126312, 'e_o_k': [0.635975, 0.508780, 0.407024, 0.325619, 0.260495], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.120617, 'e_o_k': [0.020103, 0.016082], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 143.519998
    return processors, tasks, B_BUDGET
