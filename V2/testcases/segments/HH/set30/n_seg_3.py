"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.049022, 'e_o_k': [0.028127, 0.022502, 0.018002], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 2.109402, 'e_o_k': [1.210313, 0.968250, 0.774600], 'p_i': 20, 'u_i': 1.6533},
        {'id': 2, 'e_m': 2.697147, 'e_o_k': [1.547543, 1.238034, 0.990428], 'p_i': 40, 'u_i': 4.3793},
        {'id': 3, 'e_m': 4.992978, 'e_o_k': [2.864823, 2.291859, 1.833487], 'p_i': 80, 'u_i': 2.7000},
        {'id': 4, 'e_m': 19.099547, 'e_o_k': [10.958757, 8.767005, 7.013604], 'p_i': 80, 'u_i': 2.7208},
        {'id': 5, 'e_m': 0.082986, 'e_o_k': [0.047615, 0.038092, 0.030474], 'p_i': 10, 'u_i': 2.5904},
        {'id': 6, 'e_m': 1.458740, 'e_o_k': [0.836982, 0.669586, 0.535668], 'p_i': 80, 'u_i': 1.1735},
        {'id': 7, 'e_m': 5.890191, 'e_o_k': [3.379618, 2.703694, 2.162955], 'p_i': 20, 'u_i': 1.5807},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
