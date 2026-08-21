"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.326494, 'e_o_k': [0.054416, 0.043532], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 2.769312, 'e_o_k': [0.281434, 0.225147, 0.180118, 0.144094], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 1.246346, 'e_o_k': [0.101349, 0.081079, 0.064863, 0.051891, 0.041512, 0.033210], 'p_i': 40, 'u_i': 3.0715},
        {'id': 3, 'e_m': 16.410034, 'e_o_k': [1.334409, 1.067528, 0.854022, 0.683218, 0.546574, 0.437259], 'p_i': 80, 'u_i': 2.1053},
        {'id': 4, 'e_m': 0.131840, 'e_o_k': [0.021973, 0.017579], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.399000, 'e_o_k': [0.066500, 0.053200], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.128588, 'e_o_k': [0.011476, 0.009181, 0.007344, 0.005876, 0.004700], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 3.064002, 'e_o_k': [0.376722, 0.301377, 0.241102], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 71.760000
    return processors, tasks, B_BUDGET
