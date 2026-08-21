"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600021, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600021, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.494555, 'e_o_k': [0.121532, 0.097226, 0.077781, 0.062225, 0.049780, 0.039824], 'p_i': 10, 'u_i': 2.5141},
        {'id': 1, 'e_m': 1.343320, 'e_o_k': [0.223887, 0.179109], 'p_i': 20, 'u_i': 3.5906},
        {'id': 2, 'e_m': 4.634419, 'e_o_k': [0.376856, 0.301484, 0.241188, 0.192950, 0.154360, 0.123488], 'p_i': 40, 'u_i': 2.8954},
        {'id': 3, 'e_m': 12.413377, 'e_o_k': [1.107810, 0.886248, 0.708998, 0.567199, 0.453759], 'p_i': 80, 'u_i': 2.6615},
        {'id': 4, 'e_m': 0.314643, 'e_o_k': [0.031976, 0.025581, 0.020465, 0.016372], 'p_i': 10, 'u_i': 4.2574},
        {'id': 5, 'e_m': 2.467467, 'e_o_k': [0.250759, 0.200607, 0.160486, 0.128389], 'p_i': 80, 'u_i': 4.9741},
        {'id': 6, 'e_m': 29.842631, 'e_o_k': [3.669176, 2.935341, 2.348273], 'p_i': 80, 'u_i': 2.2740},
        {'id': 7, 'e_m': 3.080409, 'e_o_k': [0.274906, 0.219924, 0.175940, 0.140752, 0.112601], 'p_i': 40, 'u_i': 2.9164},
    ]
    B_BUDGET = 119.600021
    return processors, tasks, B_BUDGET
