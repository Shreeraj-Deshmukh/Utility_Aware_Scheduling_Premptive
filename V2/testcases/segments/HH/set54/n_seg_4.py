"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.060089, 'e_o_k': [0.977007, 0.781605, 0.625284, 0.500227], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.339026, 'e_o_k': [0.160785, 0.128628, 0.102902, 0.082322], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 15.847193, 'e_o_k': [7.515607, 6.012485, 4.809988, 3.847991], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 1.762893, 'e_o_k': [0.836060, 0.668848, 0.535078, 0.428063], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.784991, 'e_o_k': [0.372285, 0.297828, 0.238263, 0.190610], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.814426, 'e_o_k': [0.386246, 0.308996, 0.247197, 0.197758], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.165452, 'e_o_k': [0.078467, 0.062773, 0.050219, 0.040175], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.989677, 'e_o_k': [0.469359, 0.375487, 0.300390, 0.240312], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
