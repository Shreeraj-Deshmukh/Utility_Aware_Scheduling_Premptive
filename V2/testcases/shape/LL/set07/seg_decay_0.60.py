"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 36, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 36, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.087909, 'e_o_k': [0.018442, 0.011065, 0.006639, 0.003984, 0.002390, 0.001434], 'p_i': 10, 'u_i': 2.1335},
        {'id': 1, 'e_m': 0.284882, 'e_o_k': [0.059765, 0.035859, 0.021515, 0.012909, 0.007746, 0.004647], 'p_i': 20, 'u_i': 1.1307},
        {'id': 2, 'e_m': 1.492482, 'e_o_k': [0.323664, 0.194199, 0.116519, 0.069912, 0.041947], 'p_i': 40, 'u_i': 4.3260},
        {'id': 3, 'e_m': 0.802400, 'e_o_k': [0.204694, 0.122816, 0.073690], 'p_i': 80, 'u_i': 4.7000},
        {'id': 4, 'e_m': 0.312685, 'e_o_k': [0.097714, 0.058628], 'p_i': 10, 'u_i': 1.4843},
        {'id': 5, 'e_m': 0.597481, 'e_o_k': [0.186713, 0.112028], 'p_i': 20, 'u_i': 4.5666},
        {'id': 6, 'e_m': 2.081442, 'e_o_k': [0.451388, 0.270833, 0.162500, 0.097500, 0.058500], 'p_i': 10, 'u_i': 2.1776},
        {'id': 7, 'e_m': 4.826900, 'e_o_k': [1.231352, 0.738811, 0.443287], 'p_i': 80, 'u_i': 3.5354},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
