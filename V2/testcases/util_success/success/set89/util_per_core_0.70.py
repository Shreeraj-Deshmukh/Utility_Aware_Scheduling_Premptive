"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440011, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440011, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.689022, 'e_o_k': [0.453568, 0.362855, 0.290284], 'p_i': 10, 'u_i': 2.9983},
        {'id': 1, 'e_m': 3.470171, 'e_o_k': [0.578362, 0.462689], 'p_i': 20, 'u_i': 1.1603},
        {'id': 2, 'e_m': 0.998241, 'e_o_k': [0.101447, 0.081158, 0.064926, 0.051941], 'p_i': 40, 'u_i': 4.9504},
        {'id': 3, 'e_m': 2.488968, 'e_o_k': [0.306021, 0.244816, 0.195853], 'p_i': 80, 'u_i': 4.4756},
        {'id': 4, 'e_m': 6.913093, 'e_o_k': [0.849970, 0.679976, 0.543981], 'p_i': 20, 'u_i': 1.0040},
        {'id': 5, 'e_m': 4.327161, 'e_o_k': [0.721194, 0.576955], 'p_i': 10, 'u_i': 3.8708},
        {'id': 6, 'e_m': 0.051120, 'e_o_k': [0.004562, 0.003650, 0.002920, 0.002336, 0.001869], 'p_i': 10, 'u_i': 4.3902},
        {'id': 7, 'e_m': 1.443069, 'e_o_k': [0.177427, 0.141941, 0.113553], 'p_i': 80, 'u_i': 4.5183},
    ]
    B_BUDGET = 167.440011
    return processors, tasks, B_BUDGET
