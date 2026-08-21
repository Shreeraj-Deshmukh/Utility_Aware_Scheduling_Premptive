"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 27, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 27, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.087664, 'e_o_k': [0.302129, 0.241703], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.391931, 'e_o_k': [0.066384, 0.053107, 0.042486, 0.033989], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 13.096144, 'e_o_k': [2.218182, 1.774545, 1.419636, 1.135709], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 7.655110, 'e_o_k': [2.126420, 1.701136], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.303823, 'e_o_k': [0.041177, 0.032941, 0.026353, 0.021082, 0.016866, 0.013493], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.754717, 'e_o_k': [0.127831, 0.102265, 0.081812, 0.065450], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 5.033151, 'e_o_k': [0.852498, 0.681999, 0.545599, 0.436479], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 2.791552, 'e_o_k': [0.572039, 0.457631, 0.366105], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
