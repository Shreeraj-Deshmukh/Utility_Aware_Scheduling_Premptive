"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399987, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399987, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.920347, 'e_o_k': [0.598432, 0.478745, 0.382996], 'p_i': 10, 'u_i': 1.9752},
        {'id': 1, 'e_m': 0.834414, 'e_o_k': [0.170986, 0.136789, 0.109431], 'p_i': 20, 'u_i': 3.9662},
        {'id': 2, 'e_m': 4.634773, 'e_o_k': [0.949749, 0.759799, 0.607839], 'p_i': 40, 'u_i': 1.9890},
        {'id': 3, 'e_m': 0.634609, 'e_o_k': [0.130043, 0.104034, 0.083227], 'p_i': 80, 'u_i': 3.3639},
        {'id': 4, 'e_m': 3.457185, 'e_o_k': [0.708440, 0.566752, 0.453401], 'p_i': 40, 'u_i': 4.7869},
        {'id': 5, 'e_m': 0.421109, 'e_o_k': [0.086293, 0.069034, 0.055227], 'p_i': 10, 'u_i': 2.7944},
        {'id': 6, 'e_m': 0.414008, 'e_o_k': [0.084838, 0.067870, 0.054296], 'p_i': 10, 'u_i': 4.7769},
        {'id': 7, 'e_m': 1.725014, 'e_o_k': [0.353486, 0.282789, 0.226231], 'p_i': 10, 'u_i': 1.3167},
    ]
    B_BUDGET = 110.399987
    return processors, tasks, B_BUDGET
