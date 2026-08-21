"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.827540, 'e_o_k': [0.785428, 0.628342], 'p_i': 10, 'u_i': 1.1650},
        {'id': 1, 'e_m': 2.999858, 'e_o_k': [0.508106, 0.406485, 0.325188, 0.260150], 'p_i': 20, 'u_i': 2.0635},
        {'id': 2, 'e_m': 7.357385, 'e_o_k': [2.043718, 1.634974], 'p_i': 40, 'u_i': 4.3065},
        {'id': 3, 'e_m': 4.404242, 'e_o_k': [0.596897, 0.477518, 0.382014, 0.305611, 0.244489, 0.195591], 'p_i': 80, 'u_i': 1.2855},
        {'id': 4, 'e_m': 5.560674, 'e_o_k': [0.753626, 0.602901, 0.482321, 0.385856, 0.308685, 0.246948], 'p_i': 80, 'u_i': 4.6522},
        {'id': 5, 'e_m': 1.175140, 'e_o_k': [0.174789, 0.139831, 0.111865, 0.089492, 0.071593], 'p_i': 20, 'u_i': 4.9928},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
