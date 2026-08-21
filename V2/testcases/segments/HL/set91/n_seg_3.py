"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.087664, 'e_o_k': [0.222882, 0.178306, 0.142644], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.391931, 'e_o_k': [0.080314, 0.064251, 0.051401], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 13.096144, 'e_o_k': [2.683636, 2.146909, 1.717527], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 7.655110, 'e_o_k': [1.568670, 1.254936, 1.003949], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.303823, 'e_o_k': [0.062259, 0.049807, 0.039846], 'p_i': 20, 'u_i': 4.2274},
        {'id': 5, 'e_m': 0.754717, 'e_o_k': [0.154655, 0.123724, 0.098979], 'p_i': 20, 'u_i': 3.9205},
        {'id': 6, 'e_m': 5.033151, 'e_o_k': [1.031383, 0.825107, 0.660085], 'p_i': 40, 'u_i': 1.6340},
        {'id': 7, 'e_m': 2.791552, 'e_o_k': [0.572039, 0.457631, 0.366105], 'p_i': 40, 'u_i': 3.9145},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
