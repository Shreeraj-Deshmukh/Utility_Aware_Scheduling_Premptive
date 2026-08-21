"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 64.400024, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1011, "set": 11, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}
"""

_SPEC = '{"B": 64.400024, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1011, "set": 11, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.533781, 'e_o_k': [0.079394, 0.063515, 0.050812, 0.040650, 0.032520], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 3.051801, 'e_o_k': [0.847723, 0.678178], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 2.268878, 'e_o_k': [0.630244, 0.504195], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 2.027473, 'e_o_k': [0.274779, 0.219823, 0.175859, 0.140687, 0.112549, 0.090040], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.174589, 'e_o_k': [0.048497, 0.038798], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.345496, 'e_o_k': [0.070798, 0.056639, 0.045311], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 2.718295, 'e_o_k': [0.460416, 0.368333, 0.294666, 0.235733], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 1.388352, 'e_o_k': [0.284498, 0.227599, 0.182079], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 64.400024
    return processors, tasks, B_BUDGET
