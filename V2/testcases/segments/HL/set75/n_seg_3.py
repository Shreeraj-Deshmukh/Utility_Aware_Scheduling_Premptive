"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.893774, 'e_o_k': [0.183150, 0.146520, 0.117216], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.002051, 'e_o_k': [0.000420, 0.000336, 0.000269], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 13.125199, 'e_o_k': [2.689590, 2.151672, 1.721338], 'p_i': 40, 'u_i': 2.6491},
        {'id': 3, 'e_m': 4.683481, 'e_o_k': [0.959730, 0.767784, 0.614227], 'p_i': 80, 'u_i': 3.7785},
        {'id': 4, 'e_m': 0.355356, 'e_o_k': [0.072819, 0.058255, 0.046604], 'p_i': 10, 'u_i': 2.0110},
        {'id': 5, 'e_m': 0.683705, 'e_o_k': [0.140104, 0.112083, 0.089666], 'p_i': 10, 'u_i': 2.7392},
        {'id': 6, 'e_m': 12.075953, 'e_o_k': [2.474581, 1.979664, 1.583732], 'p_i': 80, 'u_i': 4.5700},
        {'id': 7, 'e_m': 1.379822, 'e_o_k': [0.282750, 0.226200, 0.180960], 'p_i': 20, 'u_i': 2.3393},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
