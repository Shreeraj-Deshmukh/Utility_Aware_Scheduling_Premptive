"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399979, "H": 80, "J": 32, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 110.399979, "H": 80, "J": 32, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.711602, 'e_o_k': [0.197667, 0.158134], 'p_i': 10, 'u_i': 2.7633},
        {'id': 1, 'e_m': 1.956038, 'e_o_k': [0.265098, 0.212078, 0.169662, 0.135730, 0.108584, 0.086867], 'p_i': 20, 'u_i': 3.1688},
        {'id': 2, 'e_m': 6.578908, 'e_o_k': [1.348137, 1.078509, 0.862808], 'p_i': 40, 'u_i': 3.7705},
        {'id': 3, 'e_m': 14.898312, 'e_o_k': [3.052933, 2.442346, 1.953877], 'p_i': 80, 'u_i': 2.4357},
        {'id': 4, 'e_m': 4.819102, 'e_o_k': [0.816244, 0.652995, 0.522396, 0.417917], 'p_i': 80, 'u_i': 1.7399},
        {'id': 5, 'e_m': 0.459436, 'e_o_k': [0.062266, 0.049813, 0.039850, 0.031880, 0.025504, 0.020403], 'p_i': 10, 'u_i': 4.3140},
        {'id': 6, 'e_m': 1.319662, 'e_o_k': [0.196285, 0.157028, 0.125622, 0.100498, 0.080398], 'p_i': 20, 'u_i': 3.3669},
        {'id': 7, 'e_m': 2.163416, 'e_o_k': [0.600949, 0.480759], 'p_i': 20, 'u_i': 1.8038},
    ]
    B_BUDGET = 110.399979
    return processors, tasks, B_BUDGET
