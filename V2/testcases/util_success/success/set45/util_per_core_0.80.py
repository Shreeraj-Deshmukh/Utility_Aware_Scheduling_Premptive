"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359984, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359984, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.819142, 'e_o_k': [0.303190, 0.242552], 'p_i': 10, 'u_i': 3.2915},
        {'id': 1, 'e_m': 3.299232, 'e_o_k': [0.335288, 0.268230, 0.214584, 0.171667], 'p_i': 20, 'u_i': 3.4234},
        {'id': 2, 'e_m': 2.717411, 'e_o_k': [0.276160, 0.220928, 0.176742, 0.141394], 'p_i': 40, 'u_i': 1.9989},
        {'id': 3, 'e_m': 16.518000, 'e_o_k': [1.343189, 1.074551, 0.859641, 0.687713, 0.550170, 0.440136], 'p_i': 80, 'u_i': 4.1665},
        {'id': 4, 'e_m': 6.103736, 'e_o_k': [1.017289, 0.813831], 'p_i': 20, 'u_i': 2.8771},
        {'id': 5, 'e_m': 2.060269, 'e_o_k': [0.209377, 0.167502, 0.134001, 0.107201], 'p_i': 20, 'u_i': 3.3920},
        {'id': 6, 'e_m': 0.889975, 'e_o_k': [0.148329, 0.118663], 'p_i': 10, 'u_i': 1.7352},
        {'id': 7, 'e_m': 9.630323, 'e_o_k': [0.859441, 0.687553, 0.550042, 0.440034, 0.352027], 'p_i': 20, 'u_i': 3.3959},
    ]
    B_BUDGET = 191.359984
    return processors, tasks, B_BUDGET
