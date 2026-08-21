"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519984, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519984, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.836693, 'e_o_k': [0.149354, 0.119483, 0.095586, 0.076469, 0.061175, 0.048940], 'p_i': 10, 'u_i': 1.1682},
        {'id': 1, 'e_m': 2.456161, 'e_o_k': [0.199727, 0.159782, 0.127825, 0.102260, 0.081808, 0.065447], 'p_i': 20, 'u_i': 1.7372},
        {'id': 2, 'e_m': 3.391660, 'e_o_k': [0.275799, 0.220639, 0.176511, 0.141209, 0.112967, 0.090374], 'p_i': 40, 'u_i': 1.2016},
        {'id': 3, 'e_m': 0.041191, 'e_o_k': [0.006865, 0.005492], 'p_i': 80, 'u_i': 4.7805},
        {'id': 4, 'e_m': 2.430142, 'e_o_k': [0.298788, 0.239030, 0.191224], 'p_i': 10, 'u_i': 3.7064},
        {'id': 5, 'e_m': 4.360305, 'e_o_k': [0.726718, 0.581374], 'p_i': 10, 'u_i': 4.7396},
        {'id': 6, 'e_m': 0.092055, 'e_o_k': [0.015343, 0.012274], 'p_i': 10, 'u_i': 4.0832},
        {'id': 7, 'e_m': 1.199660, 'e_o_k': [0.107062, 0.085649, 0.068519, 0.054815, 0.043852], 'p_i': 10, 'u_i': 1.4400},
    ]
    B_BUDGET = 143.519984
    return processors, tasks, B_BUDGET
