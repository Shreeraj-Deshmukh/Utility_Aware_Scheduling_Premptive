"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.107893, 'e_o_k': [0.227027, 0.181622, 0.145298], 'p_i': 10, 'u_i': 1.6802},
        {'id': 1, 'e_m': 3.595129, 'e_o_k': [0.998647, 0.798918], 'p_i': 20, 'u_i': 4.8914},
        {'id': 2, 'e_m': 4.190122, 'e_o_k': [0.567878, 0.454302, 0.363442, 0.290754, 0.232603, 0.186082], 'p_i': 40, 'u_i': 2.7135},
        {'id': 3, 'e_m': 24.008225, 'e_o_k': [3.253782, 2.603026, 2.082420, 1.665936, 1.332749, 1.066199], 'p_i': 80, 'u_i': 1.9259},
        {'id': 4, 'e_m': 3.350223, 'e_o_k': [0.567450, 0.453960, 0.363168, 0.290534], 'p_i': 40, 'u_i': 2.2208},
        {'id': 5, 'e_m': 0.833710, 'e_o_k': [0.124005, 0.099204, 0.079363, 0.063491, 0.050792], 'p_i': 40, 'u_i': 3.1305},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
