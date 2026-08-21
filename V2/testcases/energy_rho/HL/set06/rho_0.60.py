"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680001, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.6, "seed": 1006, "set": 6, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 95.680001, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.6, "seed": 1006, "set": 6, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.123701, 'e_o_k': [0.312139, 0.249711], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 2.998422, 'e_o_k': [0.507863, 0.406290, 0.325032, 0.260026], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 12.570386, 'e_o_k': [2.129130, 1.703304, 1.362643, 1.090115], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.317492, 'e_o_k': [0.088192, 0.070554], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 2.758630, 'e_o_k': [0.467248, 0.373798, 0.299039, 0.239231], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 2.930909, 'e_o_k': [0.814141, 0.651313], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.031369, 'e_o_k': [0.004666, 0.003733, 0.002986, 0.002389, 0.001911], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.066594, 'e_o_k': [0.009905, 0.007924, 0.006339, 0.005071, 0.004057], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 95.680001
    return processors, tasks, B_BUDGET
