"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440003, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.352604, 'e_o_k': [0.031468, 0.025174, 0.020139, 0.016111, 0.012889], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 2.523202, 'e_o_k': [0.205178, 0.164143, 0.131314, 0.105051, 0.084041, 0.067233], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 15.158308, 'e_o_k': [2.526385, 2.021108], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 15.578802, 'e_o_k': [2.596467, 2.077174], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 10.488844, 'e_o_k': [1.748141, 1.398513], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 7.599222, 'e_o_k': [0.617944, 0.494355, 0.395484, 0.316387, 0.253110, 0.202488], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 2.277369, 'e_o_k': [0.379562, 0.303649], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 6.395081, 'e_o_k': [0.786280, 0.629024, 0.503219], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 167.440003
    return processors, tasks, B_BUDGET
