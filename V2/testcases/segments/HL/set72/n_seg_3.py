"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.230439, 'e_o_k': [0.047221, 0.037777, 0.030222], 'p_i': 10, 'u_i': 4.4014},
        {'id': 1, 'e_m': 1.720704, 'e_o_k': [0.352603, 0.282083, 0.225666], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 4.747157, 'e_o_k': [0.972778, 0.778222, 0.622578], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 5.488993, 'e_o_k': [1.124794, 0.899835, 0.719868], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 2.627935, 'e_o_k': [0.538511, 0.430809, 0.344647], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 2.026805, 'e_o_k': [0.415329, 0.332263, 0.265810], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 12.325637, 'e_o_k': [2.525745, 2.020596, 1.616477], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 1.238545, 'e_o_k': [0.253800, 0.203040, 0.162432], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
