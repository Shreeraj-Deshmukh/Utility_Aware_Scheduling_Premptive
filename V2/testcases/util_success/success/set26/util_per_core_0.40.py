"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679971, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679971, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.261458, 'e_o_k': [0.331449, 0.265159, 0.212127, 0.169702], 'p_i': 10, 'u_i': 2.1780},
        {'id': 1, 'e_m': 1.108892, 'e_o_k': [0.136339, 0.109071, 0.087257], 'p_i': 20, 'u_i': 3.8388},
        {'id': 2, 'e_m': 2.887856, 'e_o_k': [0.293481, 0.234785, 0.187828, 0.150262], 'p_i': 40, 'u_i': 1.0041},
        {'id': 3, 'e_m': 7.831935, 'e_o_k': [1.305323, 1.044258], 'p_i': 80, 'u_i': 4.1994},
        {'id': 4, 'e_m': 1.667341, 'e_o_k': [0.135583, 0.108466, 0.086773, 0.069418, 0.055535, 0.044428], 'p_i': 40, 'u_i': 2.8402},
        {'id': 5, 'e_m': 0.734982, 'e_o_k': [0.059766, 0.047813, 0.038250, 0.030600, 0.024480, 0.019584], 'p_i': 10, 'u_i': 1.6917},
        {'id': 6, 'e_m': 0.370506, 'e_o_k': [0.033065, 0.026452, 0.021162, 0.016929, 0.013543], 'p_i': 10, 'u_i': 1.6028},
        {'id': 7, 'e_m': 7.686534, 'e_o_k': [0.945066, 0.756053, 0.604842], 'p_i': 80, 'u_i': 2.5090},
    ]
    B_BUDGET = 95.679971
    return processors, tasks, B_BUDGET
