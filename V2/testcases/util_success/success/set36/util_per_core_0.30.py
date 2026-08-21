"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760015, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760015, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.706743, 'e_o_k': [0.063072, 0.050458, 0.040366, 0.032293, 0.025834], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.538944, 'e_o_k': [0.066264, 0.053011, 0.042409], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.566058, 'e_o_k': [0.046030, 0.036824, 0.029459, 0.023567, 0.018854, 0.015083], 'p_i': 40, 'u_i': 1.5166},
        {'id': 3, 'e_m': 3.084971, 'e_o_k': [0.514162, 0.411330], 'p_i': 80, 'u_i': 1.2517},
        {'id': 4, 'e_m': 11.919701, 'e_o_k': [1.211352, 0.969081, 0.775265, 0.620212], 'p_i': 40, 'u_i': 3.8216},
        {'id': 5, 'e_m': 2.391286, 'e_o_k': [0.294011, 0.235208, 0.188167], 'p_i': 40, 'u_i': 4.3612},
        {'id': 6, 'e_m': 0.788980, 'e_o_k': [0.080181, 0.064145, 0.051316, 0.041053], 'p_i': 10, 'u_i': 2.3108},
        {'id': 7, 'e_m': 0.519690, 'e_o_k': [0.052814, 0.042251, 0.033801, 0.027041], 'p_i': 40, 'u_i': 1.0383},
    ]
    B_BUDGET = 71.760015
    return processors, tasks, B_BUDGET
