"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.006839, 'e_o_k': [0.557455, 0.445964], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.143860, 'e_o_k': [0.039961, 0.031969], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 4.365284, 'e_o_k': [1.212579, 0.970063], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 1.921148, 'e_o_k': [0.533652, 0.426922], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 3.369376, 'e_o_k': [0.935938, 0.748750], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 1.402420, 'e_o_k': [0.389561, 0.311649], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 6.817126, 'e_o_k': [1.893646, 1.514917], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 2.194072, 'e_o_k': [0.609464, 0.487571], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
