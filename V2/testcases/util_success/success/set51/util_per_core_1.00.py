"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200021, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200021, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.314020, 'e_o_k': [0.133539, 0.106831, 0.085465, 0.068372], 'p_i': 10, 'u_i': 2.0211},
        {'id': 1, 'e_m': 4.339300, 'e_o_k': [0.533521, 0.426816, 0.341453], 'p_i': 20, 'u_i': 3.1521},
        {'id': 2, 'e_m': 1.727324, 'e_o_k': [0.140460, 0.112368, 0.089895, 0.071916, 0.057533, 0.046026], 'p_i': 40, 'u_i': 4.6880},
        {'id': 3, 'e_m': 25.049466, 'e_o_k': [2.036939, 1.629552, 1.303641, 1.042913, 0.834330, 0.667464], 'p_i': 80, 'u_i': 3.7723},
        {'id': 4, 'e_m': 5.073830, 'e_o_k': [0.845638, 0.676511], 'p_i': 20, 'u_i': 2.0383},
        {'id': 5, 'e_m': 39.170964, 'e_o_k': [3.980789, 3.184631, 2.547705, 2.038164], 'p_i': 80, 'u_i': 4.5751},
        {'id': 6, 'e_m': 9.665173, 'e_o_k': [1.610862, 1.288690], 'p_i': 20, 'u_i': 3.4615},
        {'id': 7, 'e_m': 0.687444, 'e_o_k': [0.055901, 0.044721, 0.035776, 0.028621, 0.022897, 0.018318], 'p_i': 10, 'u_i': 4.4330},
    ]
    B_BUDGET = 239.200021
    return processors, tasks, B_BUDGET
