"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.701313, 'e_o_k': [0.070131, 0.070131, 0.070131, 0.070131, 0.070131], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 6.860890, 'e_o_k': [1.143482, 1.143482, 1.143482], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.414599, 'e_o_k': [0.103650, 0.103650], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 3.429684, 'e_o_k': [0.285807, 0.285807, 0.285807, 0.285807, 0.285807, 0.285807], 'p_i': 80, 'u_i': 4.0993},
        {'id': 4, 'e_m': 1.398858, 'e_o_k': [0.349714, 0.349714], 'p_i': 20, 'u_i': 2.5958},
        {'id': 5, 'e_m': 5.494678, 'e_o_k': [0.915780, 0.915780, 0.915780], 'p_i': 80, 'u_i': 1.3643},
        {'id': 6, 'e_m': 5.102592, 'e_o_k': [0.425216, 0.425216, 0.425216, 0.425216, 0.425216, 0.425216], 'p_i': 40, 'u_i': 1.6218},
        {'id': 7, 'e_m': 5.391763, 'e_o_k': [0.673970, 0.673970, 0.673970, 0.673970], 'p_i': 80, 'u_i': 1.2955},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET
