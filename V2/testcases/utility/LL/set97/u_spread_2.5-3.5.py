"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 23, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 23, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.350656, 'e_o_k': [0.052156, 0.041725, 0.033380, 0.026704, 0.021363], 'p_i': 10, 'u_i': 3.3574},
        {'id': 1, 'e_m': 3.430445, 'e_o_k': [0.702960, 0.562368, 0.449894], 'p_i': 20, 'u_i': 2.6262},
        {'id': 2, 'e_m': 0.207300, 'e_o_k': [0.057583, 0.046067], 'p_i': 40, 'u_i': 2.8293},
        {'id': 3, 'e_m': 1.714842, 'e_o_k': [0.232409, 0.185927, 0.148742, 0.118993, 0.095195, 0.076156], 'p_i': 80, 'u_i': 3.2748},
        {'id': 4, 'e_m': 0.699429, 'e_o_k': [0.194286, 0.155429], 'p_i': 20, 'u_i': 2.8989},
        {'id': 5, 'e_m': 2.747339, 'e_o_k': [0.562979, 0.450383, 0.360307], 'p_i': 80, 'u_i': 2.5911},
        {'id': 6, 'e_m': 2.551296, 'e_o_k': [0.345772, 0.276617, 0.221294, 0.177035, 0.141628, 0.113302], 'p_i': 40, 'u_i': 2.6554},
        {'id': 7, 'e_m': 2.695881, 'e_o_k': [0.456619, 0.365296, 0.292236, 0.233789], 'p_i': 80, 'u_i': 2.5739},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
