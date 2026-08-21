"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.125769, 'e_o_k': [1.008156, 0.806525, 0.645220, 0.516176], 'p_i': 10, 'u_i': 2.8802},
        {'id': 1, 'e_m': 3.760586, 'e_o_k': [1.783476, 1.426780, 1.141424, 0.913139], 'p_i': 20, 'u_i': 1.9313},
        {'id': 2, 'e_m': 8.060220, 'e_o_k': [6.269060, 5.015248], 'p_i': 40, 'u_i': 4.0147},
        {'id': 3, 'e_m': 3.458466, 'e_o_k': [1.312411, 1.049929, 0.839943, 0.671955, 0.537564, 0.430051], 'p_i': 80, 'u_i': 3.8759},
        {'id': 4, 'e_m': 5.300970, 'e_o_k': [3.041540, 2.433232, 1.946586], 'p_i': 80, 'u_i': 4.3076},
        {'id': 5, 'e_m': 7.071626, 'e_o_k': [2.683526, 2.146820, 1.717456, 1.373965, 1.099172, 0.879338], 'p_i': 80, 'u_i': 1.9116},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
