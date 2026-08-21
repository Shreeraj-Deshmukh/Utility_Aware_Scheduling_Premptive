"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.439153, 'e_o_k': [0.176945, 0.141556, 0.113245], 'p_i': 10, 'u_i': 3.9504},
        {'id': 1, 'e_m': 2.079360, 'e_o_k': [0.185569, 0.148455, 0.118764, 0.095011, 0.076009], 'p_i': 20, 'u_i': 2.1226},
        {'id': 2, 'e_m': 0.294327, 'e_o_k': [0.049054, 0.039244], 'p_i': 40, 'u_i': 2.4300},
        {'id': 3, 'e_m': 1.315035, 'e_o_k': [0.117358, 0.093886, 0.075109, 0.060087, 0.048070], 'p_i': 80, 'u_i': 4.3958},
        {'id': 4, 'e_m': 8.960451, 'e_o_k': [0.728634, 0.582907, 0.466326, 0.373061, 0.298449, 0.238759], 'p_i': 80, 'u_i': 4.7703},
        {'id': 5, 'e_m': 0.048915, 'e_o_k': [0.003978, 0.003182, 0.002546, 0.002037, 0.001629, 0.001303], 'p_i': 80, 'u_i': 1.8568},
        {'id': 6, 'e_m': 2.000915, 'e_o_k': [0.246014, 0.196811, 0.157449], 'p_i': 20, 'u_i': 1.8128},
        {'id': 7, 'e_m': 12.626309, 'e_o_k': [2.104385, 1.683508], 'p_i': 40, 'u_i': 1.5689},
    ]
    B_BUDGET = 95.679995
    return processors, tasks, B_BUDGET
