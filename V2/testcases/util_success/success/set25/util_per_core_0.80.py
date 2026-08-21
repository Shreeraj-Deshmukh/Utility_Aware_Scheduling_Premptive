"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.36001, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.36001, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.240418, 'e_o_k': [0.019550, 0.015640, 0.012512, 0.010010, 0.008008, 0.006406], 'p_i': 10, 'u_i': 2.0799},
        {'id': 1, 'e_m': 8.924549, 'e_o_k': [1.487425, 1.189940], 'p_i': 20, 'u_i': 1.2465},
        {'id': 2, 'e_m': 9.816180, 'e_o_k': [1.206907, 0.965526, 0.772421], 'p_i': 40, 'u_i': 3.7304},
        {'id': 3, 'e_m': 34.417344, 'e_o_k': [3.497698, 2.798158, 2.238526, 1.790821], 'p_i': 80, 'u_i': 3.6440},
        {'id': 4, 'e_m': 9.742336, 'e_o_k': [0.990075, 0.792060, 0.633648, 0.506918], 'p_i': 40, 'u_i': 3.8706},
        {'id': 5, 'e_m': 0.527530, 'e_o_k': [0.053611, 0.042889, 0.034311, 0.027449], 'p_i': 10, 'u_i': 3.6333},
        {'id': 6, 'e_m': 1.251767, 'e_o_k': [0.208628, 0.166902], 'p_i': 10, 'u_i': 1.7045},
        {'id': 7, 'e_m': 0.326213, 'e_o_k': [0.026527, 0.021221, 0.016977, 0.013582, 0.010865, 0.008692], 'p_i': 10, 'u_i': 4.9475},
    ]
    B_BUDGET = 191.360010
    return processors, tasks, B_BUDGET
