"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119995, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119995, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.606861, 'e_o_k': [0.163299, 0.130639, 0.104511, 0.083609], 'p_i': 10, 'u_i': 4.8781},
        {'id': 1, 'e_m': 7.317137, 'e_o_k': [0.595005, 0.476004, 0.380803, 0.304643, 0.243714, 0.194971], 'p_i': 20, 'u_i': 1.0436},
        {'id': 2, 'e_m': 10.073637, 'e_o_k': [0.899004, 0.719203, 0.575362, 0.460290, 0.368232], 'p_i': 40, 'u_i': 2.8332},
        {'id': 3, 'e_m': 24.862871, 'e_o_k': [2.218843, 1.775074, 1.420059, 1.136047, 0.908838], 'p_i': 80, 'u_i': 2.2731},
        {'id': 4, 'e_m': 2.383232, 'e_o_k': [0.212687, 0.170150, 0.136120, 0.108896, 0.087117], 'p_i': 10, 'u_i': 1.4130},
        {'id': 5, 'e_m': 3.161058, 'e_o_k': [0.388655, 0.310924, 0.248739], 'p_i': 10, 'u_i': 3.5117},
        {'id': 6, 'e_m': 4.752768, 'e_o_k': [0.584357, 0.467485, 0.373988], 'p_i': 20, 'u_i': 4.5056},
        {'id': 7, 'e_m': 6.375256, 'e_o_k': [1.062543, 0.850034], 'p_i': 20, 'u_i': 2.8062},
    ]
    B_BUDGET = 263.119995
    return processors, tasks, B_BUDGET
