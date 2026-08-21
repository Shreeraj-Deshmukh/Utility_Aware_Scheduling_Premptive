"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.439041, 'e_o_k': [0.112000, 0.067200, 0.040320], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 0.880194, 'e_o_k': [0.184654, 0.110792, 0.066475, 0.039885, 0.023931, 0.014359], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 7.606803, 'e_o_k': [2.377126, 1.426276], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 0.610708, 'e_o_k': [0.128119, 0.076871, 0.046123, 0.027674, 0.016604, 0.009963], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 0.933835, 'e_o_k': [0.238223, 0.142934, 0.085760], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 0.975572, 'e_o_k': [0.204663, 0.122798, 0.073679, 0.044207, 0.026524, 0.015915], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 0.921104, 'e_o_k': [0.234975, 0.140985, 0.084591], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 0.583852, 'e_o_k': [0.182454, 0.109472], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
