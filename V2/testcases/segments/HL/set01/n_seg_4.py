"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255642, 'e_o_k': [0.043300, 0.034640, 0.027712, 0.022169], 'p_i': 10, 'u_i': 1.1226},
        {'id': 1, 'e_m': 5.834936, 'e_o_k': [0.988302, 0.790642, 0.632513, 0.506011], 'p_i': 20, 'u_i': 3.8598},
        {'id': 2, 'e_m': 1.030030, 'e_o_k': [0.174463, 0.139570, 0.111656, 0.089325], 'p_i': 40, 'u_i': 4.6365},
        {'id': 3, 'e_m': 1.325038, 'e_o_k': [0.224430, 0.179544, 0.143636, 0.114908], 'p_i': 80, 'u_i': 1.0760},
        {'id': 4, 'e_m': 19.367876, 'e_o_k': [3.280467, 2.624373, 2.099499, 1.679599], 'p_i': 80, 'u_i': 3.5452},
        {'id': 5, 'e_m': 0.396585, 'e_o_k': [0.067172, 0.053738, 0.042990, 0.034392], 'p_i': 40, 'u_i': 3.7479},
        {'id': 6, 'e_m': 3.226328, 'e_o_k': [0.546465, 0.437172, 0.349737, 0.279790], 'p_i': 80, 'u_i': 4.4508},
        {'id': 7, 'e_m': 2.960663, 'e_o_k': [0.501467, 0.401174, 0.320939, 0.256751], 'p_i': 20, 'u_i': 2.7382},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
