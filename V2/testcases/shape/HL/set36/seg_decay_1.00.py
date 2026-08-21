"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.942324, 'e_o_k': [0.094232, 0.094232, 0.094232, 0.094232, 0.094232], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.718592, 'e_o_k': [0.119765, 0.119765, 0.119765], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.754744, 'e_o_k': [0.062895, 0.062895, 0.062895, 0.062895, 0.062895, 0.062895], 'p_i': 40, 'u_i': 1.5166},
        {'id': 3, 'e_m': 4.113295, 'e_o_k': [1.028324, 1.028324], 'p_i': 80, 'u_i': 1.2517},
        {'id': 4, 'e_m': 15.892935, 'e_o_k': [1.986617, 1.986617, 1.986617, 1.986617], 'p_i': 40, 'u_i': 3.8216},
        {'id': 5, 'e_m': 3.188381, 'e_o_k': [0.531397, 0.531397, 0.531397], 'p_i': 40, 'u_i': 4.3612},
        {'id': 6, 'e_m': 1.051973, 'e_o_k': [0.131497, 0.131497, 0.131497, 0.131497], 'p_i': 10, 'u_i': 2.3108},
        {'id': 7, 'e_m': 0.692921, 'e_o_k': [0.086615, 0.086615, 0.086615, 0.086615], 'p_i': 40, 'u_i': 1.0383},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
