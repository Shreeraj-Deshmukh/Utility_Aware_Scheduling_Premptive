"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360011, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360011, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.460879, 'e_o_k': [0.037477, 0.029982, 0.023985, 0.019188, 0.015351, 0.012281], 'p_i': 10, 'u_i': 2.8095},
        {'id': 1, 'e_m': 3.441408, 'e_o_k': [0.423124, 0.338499, 0.270799], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 9.494313, 'e_o_k': [0.847303, 0.677842, 0.542274, 0.433819, 0.347055], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 10.977986, 'e_o_k': [1.349752, 1.079802, 0.863841], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 5.255870, 'e_o_k': [0.469051, 0.375241, 0.300193, 0.240154, 0.192123], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 4.053610, 'e_o_k': [0.361757, 0.289406, 0.231525, 0.185220, 0.148176], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 24.651274, 'e_o_k': [2.199959, 1.759967, 1.407974, 1.126379, 0.901103], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 2.477090, 'e_o_k': [0.304560, 0.243648, 0.194919], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 191.360011
    return processors, tasks, B_BUDGET
