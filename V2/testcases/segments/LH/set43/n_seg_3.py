"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320013, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320013, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.025820, 'e_o_k': [0.014815, 0.011852, 0.009482], 'p_i': 10, 'u_i': 4.0574},
        {'id': 1, 'e_m': 1.233166, 'e_o_k': [0.707554, 0.566043, 0.452835], 'p_i': 20, 'u_i': 2.7090},
        {'id': 2, 'e_m': 1.873854, 'e_o_k': [1.075162, 0.860130, 0.688104], 'p_i': 40, 'u_i': 3.6072},
        {'id': 3, 'e_m': 2.076895, 'e_o_k': [1.191661, 0.953329, 0.762663], 'p_i': 80, 'u_i': 4.0494},
        {'id': 4, 'e_m': 0.193184, 'e_o_k': [0.110844, 0.088675, 0.070940], 'p_i': 20, 'u_i': 4.5815},
        {'id': 5, 'e_m': 2.190958, 'e_o_k': [1.257107, 1.005686, 0.804549], 'p_i': 20, 'u_i': 1.1362},
        {'id': 6, 'e_m': 0.888908, 'e_o_k': [0.510029, 0.408023, 0.326419], 'p_i': 80, 'u_i': 3.3217},
        {'id': 7, 'e_m': 5.305348, 'e_o_k': [3.044052, 2.435241, 1.948193], 'p_i': 40, 'u_i': 1.1761},
    ]
    B_BUDGET = 88.320013
    return processors, tasks, B_BUDGET
