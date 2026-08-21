"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760018, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760018, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.825077, 'e_o_k': [0.162876, 0.130301, 0.104240, 0.083392, 0.066714], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 1.258998, 'e_o_k': [0.127947, 0.102358, 0.081886, 0.065509], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 2.023288, 'e_o_k': [0.337215, 0.269772], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 4.187563, 'e_o_k': [0.340519, 0.272415, 0.217932, 0.174346, 0.139476, 0.111581], 'p_i': 80, 'u_i': 3.6642},
        {'id': 4, 'e_m': 0.719975, 'e_o_k': [0.073168, 0.058535, 0.046828, 0.037462], 'p_i': 10, 'u_i': 2.6174},
        {'id': 5, 'e_m': 0.900275, 'e_o_k': [0.080343, 0.064275, 0.051420, 0.041136, 0.032909], 'p_i': 10, 'u_i': 2.3254},
        {'id': 6, 'e_m': 0.146496, 'e_o_k': [0.024416, 0.019533], 'p_i': 10, 'u_i': 3.2626},
        {'id': 7, 'e_m': 2.997644, 'e_o_k': [0.267519, 0.214016, 0.171212, 0.136970, 0.109576], 'p_i': 40, 'u_i': 1.6837},
    ]
    B_BUDGET = 71.760018
    return processors, tasks, B_BUDGET
