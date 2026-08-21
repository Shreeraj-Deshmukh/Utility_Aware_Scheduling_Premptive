"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399984, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399984, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.049022, 'e_o_k': [0.010046, 0.008036, 0.006429], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 2.109402, 'e_o_k': [0.432255, 0.345804, 0.276643], 'p_i': 20, 'u_i': 1.6533},
        {'id': 2, 'e_m': 2.697147, 'e_o_k': [0.552694, 0.442155, 0.353724], 'p_i': 40, 'u_i': 4.3793},
        {'id': 3, 'e_m': 4.992978, 'e_o_k': [1.023151, 0.818521, 0.654817], 'p_i': 80, 'u_i': 2.7000},
        {'id': 4, 'e_m': 19.099547, 'e_o_k': [3.913842, 3.131073, 2.504859], 'p_i': 80, 'u_i': 2.7208},
        {'id': 5, 'e_m': 0.082986, 'e_o_k': [0.017005, 0.013604, 0.010883], 'p_i': 10, 'u_i': 2.5904},
        {'id': 6, 'e_m': 1.458740, 'e_o_k': [0.298922, 0.239138, 0.191310], 'p_i': 80, 'u_i': 1.1735},
        {'id': 7, 'e_m': 5.890191, 'e_o_k': [1.207006, 0.965605, 0.772484], 'p_i': 20, 'u_i': 1.5807},
    ]
    B_BUDGET = 110.399984
    return processors, tasks, B_BUDGET
