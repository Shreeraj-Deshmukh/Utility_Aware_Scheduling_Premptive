"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.415674, 'e_o_k': [2.197584, 1.318551, 0.791130, 0.474678], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.148832, 'e_o_k': [0.090373, 0.054224, 0.032534, 0.019521, 0.011712], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 2.086145, 'e_o_k': [1.266743, 0.760046, 0.456028, 0.273617, 0.164170], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 0.844474, 'e_o_k': [0.738915, 0.443349], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 1.893474, 'e_o_k': [1.656790, 0.994074], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 1.089996, 'e_o_k': [0.953747, 0.572248], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 2.548948, 'e_o_k': [1.639948, 0.983969, 0.590381, 0.354229], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.028745, 'e_o_k': [0.018494, 0.011096, 0.006658, 0.003995], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
