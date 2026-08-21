"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 80.959994, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.2, "seed": 1002, "set": 2, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.20"}
"""

_SPEC = '{"B": 80.959994, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.2, "seed": 1002, "set": 2, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.20"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.711602, 'e_o_k': [0.197667, 0.158134], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 1.956038, 'e_o_k': [0.265098, 0.212078, 0.169662, 0.135730, 0.108584, 0.086867], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 6.578908, 'e_o_k': [1.348137, 1.078509, 0.862808], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 14.898312, 'e_o_k': [3.052933, 2.442346, 1.953877], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 4.819102, 'e_o_k': [0.816244, 0.652995, 0.522396, 0.417917], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.459436, 'e_o_k': [0.062266, 0.049813, 0.039850, 0.031880, 0.025504, 0.020403], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 1.319662, 'e_o_k': [0.196285, 0.157028, 0.125622, 0.100498, 0.080398], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 2.163416, 'e_o_k': [0.600949, 0.480759], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 80.959994
    return processors, tasks, B_BUDGET
