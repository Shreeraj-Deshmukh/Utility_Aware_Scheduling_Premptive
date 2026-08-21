"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360016, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360016, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.671676, 'e_o_k': [0.373138, 0.298510, 0.238808, 0.191047], 'p_i': 10, 'u_i': 2.7515},
        {'id': 1, 'e_m': 6.317157, 'e_o_k': [1.052860, 0.842288], 'p_i': 20, 'u_i': 4.8495},
        {'id': 2, 'e_m': 11.713496, 'e_o_k': [1.190396, 0.952317, 0.761853, 0.609483], 'p_i': 40, 'u_i': 3.9350},
        {'id': 3, 'e_m': 21.155600, 'e_o_k': [3.525933, 2.820747], 'p_i': 80, 'u_i': 4.4741},
        {'id': 4, 'e_m': 4.014902, 'e_o_k': [0.669150, 0.535320], 'p_i': 40, 'u_i': 1.8290},
        {'id': 5, 'e_m': 2.174532, 'e_o_k': [0.362422, 0.289938], 'p_i': 10, 'u_i': 3.8600},
        {'id': 6, 'e_m': 1.614825, 'e_o_k': [0.198544, 0.158835, 0.127068], 'p_i': 80, 'u_i': 4.0344},
        {'id': 7, 'e_m': 0.216812, 'e_o_k': [0.036135, 0.028908], 'p_i': 10, 'u_i': 3.0439},
    ]
    B_BUDGET = 191.360016
    return processors, tasks, B_BUDGET
