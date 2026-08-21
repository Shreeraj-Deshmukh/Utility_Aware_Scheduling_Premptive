"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.439386, 'e_o_k': [0.122052, 0.097641], 'p_i': 10, 'u_i': 3.0447},
        {'id': 1, 'e_m': 3.381221, 'e_o_k': [0.939228, 0.751382], 'p_i': 20, 'u_i': 2.1118},
        {'id': 2, 'e_m': 4.501107, 'e_o_k': [1.250307, 1.000246], 'p_i': 40, 'u_i': 4.2305},
        {'id': 3, 'e_m': 1.296672, 'e_o_k': [0.360187, 0.288149], 'p_i': 80, 'u_i': 2.0791},
        {'id': 4, 'e_m': 14.537940, 'e_o_k': [4.038317, 3.230653], 'p_i': 80, 'u_i': 1.4810},
        {'id': 5, 'e_m': 7.948216, 'e_o_k': [2.207838, 1.766270], 'p_i': 80, 'u_i': 3.5439},
        {'id': 6, 'e_m': 7.236118, 'e_o_k': [2.010033, 1.608026], 'p_i': 80, 'u_i': 1.8113},
        {'id': 7, 'e_m': 0.867358, 'e_o_k': [0.240933, 0.192746], 'p_i': 10, 'u_i': 4.9983},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
