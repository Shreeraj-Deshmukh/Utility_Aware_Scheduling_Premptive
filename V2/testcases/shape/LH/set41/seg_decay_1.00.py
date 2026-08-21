"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320009, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320009, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.439041, 'e_o_k': [0.204886, 0.204886, 0.204886], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 0.880194, 'e_o_k': [0.205379, 0.205379, 0.205379, 0.205379, 0.205379, 0.205379], 'p_i': 20, 'u_i': 3.7145},
        {'id': 2, 'e_m': 7.606803, 'e_o_k': [5.324762, 5.324762], 'p_i': 40, 'u_i': 2.6488},
        {'id': 3, 'e_m': 0.610708, 'e_o_k': [0.142498, 0.142498, 0.142498, 0.142498, 0.142498, 0.142498], 'p_i': 80, 'u_i': 4.3024},
        {'id': 4, 'e_m': 0.933835, 'e_o_k': [0.435790, 0.435790, 0.435790], 'p_i': 20, 'u_i': 4.8206},
        {'id': 5, 'e_m': 0.975572, 'e_o_k': [0.227633, 0.227633, 0.227633, 0.227633, 0.227633, 0.227633], 'p_i': 20, 'u_i': 3.2508},
        {'id': 6, 'e_m': 0.921104, 'e_o_k': [0.429848, 0.429848, 0.429848], 'p_i': 80, 'u_i': 3.3334},
        {'id': 7, 'e_m': 0.583852, 'e_o_k': [0.408697, 0.408697], 'p_i': 80, 'u_i': 2.1081},
    ]
    B_BUDGET = 88.320009
    return processors, tasks, B_BUDGET
