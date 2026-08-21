"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.172365, 0.137892], 'p_i': 10, 'u_i': 2.5678},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.149737, 0.119789], 'p_i': 20, 'u_i': 3.0744},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [2.794926, 2.235941], 'p_i': 40, 'u_i': 3.1102},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [8.019166, 6.415333], 'p_i': 80, 'u_i': 3.9862},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.564488, 0.451590], 'p_i': 20, 'u_i': 1.5757},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.523561, 0.418849], 'p_i': 10, 'u_i': 4.9941},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.804198, 0.643358], 'p_i': 40, 'u_i': 1.7632},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.623586, 0.498869], 'p_i': 40, 'u_i': 1.4284},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
