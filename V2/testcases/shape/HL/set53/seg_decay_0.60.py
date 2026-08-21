"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399988, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399988, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.318061, 'e_o_k': [0.099394, 0.059636], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 2.437651, 'e_o_k': [0.761766, 0.457060], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 1.991584, 'e_o_k': [0.431901, 0.259141, 0.155485, 0.093291, 0.055974], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 10.739727, 'e_o_k': [3.356165, 2.013699], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 1.836977, 'e_o_k': [0.385375, 0.231225, 0.138735, 0.083241, 0.049945, 0.029967], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 1.702926, 'e_o_k': [0.391297, 0.234778, 0.140867, 0.084520], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 2.860437, 'e_o_k': [0.657270, 0.394362, 0.236617, 0.141970], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 8.242902, 'e_o_k': [1.729261, 1.037557, 0.622534, 0.373520, 0.224112, 0.134467], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 110.399988
    return processors, tasks, B_BUDGET
