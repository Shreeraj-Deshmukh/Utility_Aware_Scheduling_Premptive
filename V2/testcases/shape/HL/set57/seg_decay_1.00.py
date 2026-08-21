"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.201488, 'e_o_k': [0.020149, 0.020149, 0.020149, 0.020149, 0.020149], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.441830, 'e_o_k': [0.120152, 0.120152, 0.120152, 0.120152, 0.120152, 0.120152], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 8.661890, 'e_o_k': [2.165473, 2.165473], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 8.902172, 'e_o_k': [2.225543, 2.225543], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 5.993625, 'e_o_k': [1.498406, 1.498406], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 4.342413, 'e_o_k': [0.361868, 0.361868, 0.361868, 0.361868, 0.361868, 0.361868], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 1.301354, 'e_o_k': [0.325338, 0.325338], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 3.654332, 'e_o_k': [0.609055, 0.609055, 0.609055], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET
