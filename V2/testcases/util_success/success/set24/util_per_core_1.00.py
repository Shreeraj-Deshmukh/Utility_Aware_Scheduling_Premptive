"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200015, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200015, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.897563, 'e_o_k': [0.235620, 0.188496, 0.150797, 0.120638, 0.096510, 0.077208], 'p_i': 10, 'u_i': 1.0948},
        {'id': 1, 'e_m': 0.771792, 'e_o_k': [0.068877, 0.055102, 0.044081, 0.035265, 0.028212], 'p_i': 20, 'u_i': 4.2236},
        {'id': 2, 'e_m': 12.034413, 'e_o_k': [2.005736, 1.604588], 'p_i': 40, 'u_i': 4.6411},
        {'id': 3, 'e_m': 28.447171, 'e_o_k': [3.497603, 2.798082, 2.238466], 'p_i': 80, 'u_i': 4.0085},
        {'id': 4, 'e_m': 4.946169, 'e_o_k': [0.608136, 0.486508, 0.389207], 'p_i': 10, 'u_i': 4.7538},
        {'id': 5, 'e_m': 0.452955, 'e_o_k': [0.046032, 0.036826, 0.029460, 0.023568], 'p_i': 20, 'u_i': 2.8454},
        {'id': 6, 'e_m': 3.556095, 'e_o_k': [0.289170, 0.231336, 0.185069, 0.148055, 0.118444, 0.094755], 'p_i': 10, 'u_i': 1.6966},
        {'id': 7, 'e_m': 11.386406, 'e_o_k': [1.016160, 0.812928, 0.650342, 0.520274, 0.416219], 'p_i': 80, 'u_i': 1.2435},
    ]
    B_BUDGET = 239.200015
    return processors, tasks, B_BUDGET
