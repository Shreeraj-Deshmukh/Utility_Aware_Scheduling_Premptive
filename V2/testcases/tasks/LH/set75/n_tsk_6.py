"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.611335, 'e_o_k': [0.289928, 0.231943, 0.185554, 0.148443], 'p_i': 10, 'u_i': 4.4576},
        {'id': 1, 'e_m': 0.001467, 'e_o_k': [0.001141, 0.000913], 'p_i': 20, 'u_i': 1.2102},
        {'id': 2, 'e_m': 8.726195, 'e_o_k': [5.006833, 4.005467, 3.204373], 'p_i': 40, 'u_i': 3.7306},
        {'id': 3, 'e_m': 2.728921, 'e_o_k': [1.565774, 1.252619, 1.002095], 'p_i': 80, 'u_i': 4.1325},
        {'id': 4, 'e_m': 0.509449, 'e_o_k': [0.241609, 0.193287, 0.154630, 0.123704], 'p_i': 20, 'u_i': 2.4718},
        {'id': 5, 'e_m': 2.442173, 'e_o_k': [0.926750, 0.741400, 0.593120, 0.474496, 0.379597, 0.303678], 'p_i': 40, 'u_i': 1.1369},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
