"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519998, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519998, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.394634, 'e_o_k': [0.113407, 0.090726, 0.072580, 0.058064, 0.046452, 0.037161], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.085317, 'e_o_k': [0.006938, 0.005550, 0.004440, 0.003552, 0.002842, 0.002273], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 3.935991, 'e_o_k': [0.655998, 0.524799], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 6.712009, 'e_o_k': [1.118668, 0.894935], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 3.524502, 'e_o_k': [0.587417, 0.469934], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 15.814483, 'e_o_k': [1.607163, 1.285730, 1.028584, 0.822867], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.513684, 'e_o_k': [0.085614, 0.068491], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 5.020306, 'e_o_k': [0.836718, 0.669374], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 143.519998
    return processors, tasks, B_BUDGET
