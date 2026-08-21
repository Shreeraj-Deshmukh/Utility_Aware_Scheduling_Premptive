"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119998, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119998, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.562933, 'e_o_k': [0.050238, 0.040190, 0.032152, 0.025722, 0.020577], 'p_i': 10, 'u_i': 2.1055},
        {'id': 1, 'e_m': 9.594915, 'e_o_k': [1.599152, 1.279322], 'p_i': 20, 'u_i': 4.2798},
        {'id': 2, 'e_m': 8.915501, 'e_o_k': [0.906047, 0.724837, 0.579870, 0.463896], 'p_i': 40, 'u_i': 2.6537},
        {'id': 3, 'e_m': 33.625649, 'e_o_k': [3.000861, 2.400689, 1.920551, 1.536441, 1.229153], 'p_i': 80, 'u_i': 3.1150},
        {'id': 4, 'e_m': 24.893107, 'e_o_k': [4.148851, 3.319081], 'p_i': 80, 'u_i': 3.0244},
        {'id': 5, 'e_m': 4.469956, 'e_o_k': [0.454264, 0.363411, 0.290729, 0.232583], 'p_i': 20, 'u_i': 3.4233},
        {'id': 6, 'e_m': 3.563555, 'e_o_k': [0.362150, 0.289720, 0.231776, 0.185421], 'p_i': 10, 'u_i': 1.5272},
        {'id': 7, 'e_m': 10.378856, 'e_o_k': [1.276089, 1.020871, 0.816697], 'p_i': 80, 'u_i': 1.5097},
    ]
    B_BUDGET = 263.119998
    return processors, tasks, B_BUDGET
