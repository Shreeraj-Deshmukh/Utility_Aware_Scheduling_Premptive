"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 23, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "freq", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 23, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "freq", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100443, 'e_o_k': [0.020583, 0.016466, 0.013173], 'p_i': 10, 'u_i': 2.4144},
        {'id': 1, 'e_m': 0.413851, 'e_o_k': [0.114959, 0.091967], 'p_i': 20, 'u_i': 2.6559},
        {'id': 2, 'e_m': 2.380758, 'e_o_k': [0.354111, 0.283289, 0.226631, 0.181305, 0.145044], 'p_i': 40, 'u_i': 2.8681},
        {'id': 3, 'e_m': 13.943895, 'e_o_k': [3.873304, 3.098643], 'p_i': 80, 'u_i': 1.8896},
        {'id': 4, 'e_m': 1.101724, 'e_o_k': [0.163869, 0.131095, 0.104876, 0.083901, 0.067121], 'p_i': 20, 'u_i': 1.6645},
        {'id': 5, 'e_m': 0.583734, 'e_o_k': [0.086824, 0.069459, 0.055567, 0.044454, 0.035563], 'p_i': 40, 'u_i': 1.3774},
        {'id': 6, 'e_m': 3.223359, 'e_o_k': [0.895377, 0.716302], 'p_i': 80, 'u_i': 1.9412},
        {'id': 7, 'e_m': 34.037914, 'e_o_k': [9.454976, 7.563981], 'p_i': 80, 'u_i': 2.2237},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
