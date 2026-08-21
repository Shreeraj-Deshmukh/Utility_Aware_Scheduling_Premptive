"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.992831, 'e_o_k': [0.134556, 0.107645, 0.086116, 0.068893, 0.055114, 0.044091], 'p_i': 10, 'u_i': 2.9591},
        {'id': 1, 'e_m': 4.212824, 'e_o_k': [0.626610, 0.501288, 0.401030, 0.320824, 0.256659], 'p_i': 20, 'u_i': 3.3490},
        {'id': 2, 'e_m': 13.197470, 'e_o_k': [3.665964, 2.932771], 'p_i': 40, 'u_i': 1.0216},
        {'id': 3, 'e_m': 4.415523, 'e_o_k': [0.904820, 0.723856, 0.579085], 'p_i': 80, 'u_i': 4.0085},
        {'id': 4, 'e_m': 0.055512, 'e_o_k': [0.011376, 0.009100, 0.007280], 'p_i': 20, 'u_i': 1.9931},
        {'id': 5, 'e_m': 8.173545, 'e_o_k': [1.674907, 1.339925, 1.071940], 'p_i': 80, 'u_i': 2.4773},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
