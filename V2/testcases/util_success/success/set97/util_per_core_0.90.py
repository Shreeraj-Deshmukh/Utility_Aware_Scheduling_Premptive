"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279979, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279979, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.460916, 'e_o_k': [0.118797, 0.095037, 0.076030, 0.060824, 0.048659, 0.038927], 'p_i': 10, 'u_i': 4.0993},
        {'id': 1, 'e_m': 1.438449, 'e_o_k': [0.239741, 0.191793], 'p_i': 20, 'u_i': 2.5958},
        {'id': 2, 'e_m': 17.223412, 'e_o_k': [2.117633, 1.694106, 1.355285], 'p_i': 40, 'u_i': 1.3643},
        {'id': 3, 'e_m': 15.479008, 'e_o_k': [1.258702, 1.006961, 0.805569, 0.644455, 0.515564, 0.412451], 'p_i': 80, 'u_i': 1.6218},
        {'id': 4, 'e_m': 6.969528, 'e_o_k': [0.708285, 0.566628, 0.453303, 0.362642], 'p_i': 20, 'u_i': 1.2955},
        {'id': 5, 'e_m': 1.845713, 'e_o_k': [0.187572, 0.150058, 0.120046, 0.096037], 'p_i': 10, 'u_i': 2.7520},
        {'id': 6, 'e_m': 13.634734, 'e_o_k': [1.216808, 0.973446, 0.778757, 0.623005, 0.498404], 'p_i': 40, 'u_i': 2.0302},
        {'id': 7, 'e_m': 0.839970, 'e_o_k': [0.103275, 0.082620, 0.066096], 'p_i': 10, 'u_i': 2.5969},
    ]
    B_BUDGET = 215.279979
    return processors, tasks, B_BUDGET
