"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760009, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760009, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.297006, 'e_o_k': [0.026506, 0.021205, 0.016964, 0.013571, 0.010857], 'p_i': 10, 'u_i': 2.2582},
        {'id': 1, 'e_m': 1.078644, 'e_o_k': [0.179774, 0.143819], 'p_i': 20, 'u_i': 2.9332},
        {'id': 2, 'e_m': 0.130619, 'e_o_k': [0.016060, 0.012848, 0.010278], 'p_i': 40, 'u_i': 1.0372},
        {'id': 3, 'e_m': 1.659879, 'e_o_k': [0.204083, 0.163267, 0.130613], 'p_i': 80, 'u_i': 1.7921},
        {'id': 4, 'e_m': 6.307998, 'e_o_k': [0.512945, 0.410356, 0.328285, 0.262628, 0.210102, 0.168082], 'p_i': 40, 'u_i': 1.1296},
        {'id': 5, 'e_m': 10.514253, 'e_o_k': [1.292736, 1.034189, 0.827351], 'p_i': 40, 'u_i': 3.7636},
        {'id': 6, 'e_m': 1.101467, 'e_o_k': [0.089568, 0.071654, 0.057323, 0.045859, 0.036687, 0.029350], 'p_i': 80, 'u_i': 2.3342},
        {'id': 7, 'e_m': 4.642291, 'e_o_k': [0.414293, 0.331434, 0.265148, 0.212118, 0.169694], 'p_i': 80, 'u_i': 1.6627},
    ]
    B_BUDGET = 71.760009
    return processors, tasks, B_BUDGET
