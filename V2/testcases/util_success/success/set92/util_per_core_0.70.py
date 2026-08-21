"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440016, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440016, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.978376, 'e_o_k': [0.087313, 0.069851, 0.055881, 0.044704, 0.035764], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 2.826217, 'e_o_k': [0.229819, 0.183855, 0.147084, 0.117667, 0.094134, 0.075307], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 11.126579, 'e_o_k': [1.368022, 1.094418, 0.875534], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 27.213190, 'e_o_k': [2.765568, 2.212454, 1.769964, 1.415971], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.006412, 'e_o_k': [0.001069, 0.000855], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 6.781764, 'e_o_k': [0.833823, 0.667059, 0.533647], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 1.264618, 'e_o_k': [0.128518, 0.102815, 0.082252, 0.065801], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 13.225887, 'e_o_k': [1.344094, 1.075275, 0.860220, 0.688176], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 167.440016
    return processors, tasks, B_BUDGET
