"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520006, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520006, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.041254, 'e_o_k': [0.006876, 0.005501], 'p_i': 10, 'u_i': 3.6748},
        {'id': 1, 'e_m': 1.749848, 'e_o_k': [0.291641, 0.233313], 'p_i': 20, 'u_i': 4.5666},
        {'id': 2, 'e_m': 4.882216, 'e_o_k': [0.435705, 0.348564, 0.278851, 0.223081, 0.178465], 'p_i': 40, 'u_i': 2.1776},
        {'id': 3, 'e_m': 14.410505, 'e_o_k': [1.771783, 1.417427, 1.133941], 'p_i': 80, 'u_i': 3.5354},
        {'id': 4, 'e_m': 22.133401, 'e_o_k': [2.249329, 1.799463, 1.439571, 1.151657], 'p_i': 80, 'u_i': 3.2835},
        {'id': 5, 'e_m': 0.532382, 'e_o_k': [0.088730, 0.070984], 'p_i': 20, 'u_i': 1.9722},
        {'id': 6, 'e_m': 9.729425, 'e_o_k': [1.621571, 1.297257], 'p_i': 20, 'u_i': 1.1966},
        {'id': 7, 'e_m': 0.164376, 'e_o_k': [0.014669, 0.011736, 0.009388, 0.007511, 0.006009], 'p_i': 10, 'u_i': 1.4854},
    ]
    B_BUDGET = 143.520006
    return processors, tasks, B_BUDGET
