"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.878081, 'e_o_k': [0.243911, 0.195129], 'p_i': 10, 'u_i': 1.3531},
        {'id': 1, 'e_m': 1.760389, 'e_o_k': [0.488997, 0.391197], 'p_i': 20, 'u_i': 2.6488},
        {'id': 2, 'e_m': 15.213605, 'e_o_k': [4.226002, 3.380801], 'p_i': 40, 'u_i': 4.8206},
        {'id': 3, 'e_m': 1.221415, 'e_o_k': [0.339282, 0.271426], 'p_i': 80, 'u_i': 3.3334},
        {'id': 4, 'e_m': 1.867670, 'e_o_k': [0.518797, 0.415038], 'p_i': 20, 'u_i': 2.1081},
        {'id': 5, 'e_m': 1.951144, 'e_o_k': [0.541984, 0.433588], 'p_i': 20, 'u_i': 1.8691},
        {'id': 6, 'e_m': 1.842208, 'e_o_k': [0.511724, 0.409380], 'p_i': 80, 'u_i': 3.0834},
        {'id': 7, 'e_m': 1.167704, 'e_o_k': [0.324362, 0.259490], 'p_i': 80, 'u_i': 3.6806},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
