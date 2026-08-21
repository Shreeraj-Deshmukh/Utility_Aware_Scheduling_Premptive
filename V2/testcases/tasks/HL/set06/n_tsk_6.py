"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399975, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399975, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.527669, 'e_o_k': [0.207042, 0.165633, 0.132507, 0.106005, 0.084804, 0.067843], 'p_i': 10, 'u_i': 4.5754},
        {'id': 1, 'e_m': 3.993502, 'e_o_k': [0.676406, 0.541125, 0.432900, 0.346320], 'p_i': 20, 'u_i': 3.5388},
        {'id': 2, 'e_m': 13.759506, 'e_o_k': [1.864796, 1.491836, 1.193469, 0.954775, 0.763820, 0.611056], 'p_i': 40, 'u_i': 1.2818},
        {'id': 3, 'e_m': 0.291706, 'e_o_k': [0.081029, 0.064823], 'p_i': 80, 'u_i': 2.2300},
        {'id': 4, 'e_m': 0.676970, 'e_o_k': [0.114663, 0.091730, 0.073384, 0.058707], 'p_i': 10, 'u_i': 1.1980},
        {'id': 5, 'e_m': 0.644539, 'e_o_k': [0.109170, 0.087336, 0.069869, 0.055895], 'p_i': 20, 'u_i': 3.9540},
    ]
    B_BUDGET = 110.399975
    return processors, tasks, B_BUDGET
