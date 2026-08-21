"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.049022, 'e_o_k': [0.038128, 0.030503], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 2.109402, 'e_o_k': [1.640646, 1.312517], 'p_i': 20, 'u_i': 1.6533},
        {'id': 2, 'e_m': 2.697147, 'e_o_k': [2.097781, 1.678225], 'p_i': 40, 'u_i': 4.3793},
        {'id': 3, 'e_m': 4.992978, 'e_o_k': [3.883427, 3.106742], 'p_i': 80, 'u_i': 2.7000},
        {'id': 4, 'e_m': 19.099547, 'e_o_k': [14.855203, 11.884163], 'p_i': 80, 'u_i': 2.7208},
        {'id': 5, 'e_m': 0.082986, 'e_o_k': [0.064545, 0.051636], 'p_i': 10, 'u_i': 2.5904},
        {'id': 6, 'e_m': 1.458740, 'e_o_k': [1.134575, 0.907660], 'p_i': 80, 'u_i': 1.1735},
        {'id': 7, 'e_m': 5.890191, 'e_o_k': [4.581260, 3.665008], 'p_i': 20, 'u_i': 1.5807},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
