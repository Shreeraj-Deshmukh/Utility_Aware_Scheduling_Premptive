"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280016, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280016, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.453348, 'e_o_k': [0.040458, 0.032367, 0.025893, 0.020715, 0.016572], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 3.244117, 'e_o_k': [0.263801, 0.211041, 0.168833, 0.135066, 0.108053, 0.086442], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 19.489253, 'e_o_k': [3.248209, 2.598567], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 20.029888, 'e_o_k': [3.338315, 2.670652], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 13.485657, 'e_o_k': [2.247609, 1.798088], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 9.770429, 'e_o_k': [0.794499, 0.635599, 0.508479, 0.406783, 0.325427, 0.260341], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 2.928046, 'e_o_k': [0.488008, 0.390406], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 8.222246, 'e_o_k': [1.010932, 0.808746, 0.646996], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 215.280016
    return processors, tasks, B_BUDGET
