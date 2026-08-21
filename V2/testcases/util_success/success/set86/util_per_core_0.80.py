"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360005, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360005, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.243632, 'e_o_k': [0.152906, 0.122324, 0.097860], 'p_i': 10, 'u_i': 2.6742},
        {'id': 1, 'e_m': 0.566201, 'e_o_k': [0.046042, 0.036833, 0.029467, 0.023573, 0.018859, 0.015087], 'p_i': 20, 'u_i': 1.0126},
        {'id': 2, 'e_m': 1.309533, 'e_o_k': [0.116867, 0.093494, 0.074795, 0.059836, 0.047869], 'p_i': 40, 'u_i': 1.6645},
        {'id': 3, 'e_m': 29.187130, 'e_o_k': [2.604753, 2.083803, 1.667042, 1.333634, 1.066907], 'p_i': 80, 'u_i': 1.3774},
        {'id': 4, 'e_m': 7.366570, 'e_o_k': [1.227762, 0.982209], 'p_i': 40, 'u_i': 1.9412},
        {'id': 5, 'e_m': 1.714018, 'e_o_k': [0.285670, 0.228536], 'p_i': 10, 'u_i': 2.2237},
        {'id': 6, 'e_m': 3.810440, 'e_o_k': [0.468497, 0.374797, 0.299838], 'p_i': 10, 'u_i': 2.4269},
        {'id': 7, 'e_m': 25.051133, 'e_o_k': [2.545847, 2.036677, 1.629342, 1.303474], 'p_i': 80, 'u_i': 4.8879},
    ]
    B_BUDGET = 191.360005
    return processors, tasks, B_BUDGET
