"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.543832, 'e_o_k': [0.111441, 0.089153, 0.071322], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.195966, 'e_o_k': [0.040157, 0.032126, 0.025700], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 6.548072, 'e_o_k': [1.341818, 1.073454, 0.858764], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 3.827555, 'e_o_k': [0.784335, 0.627468, 0.501974], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.151912, 'e_o_k': [0.031129, 0.024904, 0.019923], 'p_i': 20, 'u_i': 4.2274},
        {'id': 5, 'e_m': 0.377358, 'e_o_k': [0.077328, 0.061862, 0.049490], 'p_i': 20, 'u_i': 3.9205},
        {'id': 6, 'e_m': 2.516575, 'e_o_k': [0.515692, 0.412553, 0.330043], 'p_i': 40, 'u_i': 1.6340},
        {'id': 7, 'e_m': 1.395776, 'e_o_k': [0.286020, 0.228816, 0.183053], 'p_i': 40, 'u_i': 3.9145},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET
