"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.686544, 'e_o_k': [0.140685, 0.112548, 0.090039], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 1.582739, 'e_o_k': [0.324332, 0.259465, 0.207572], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 5.107137, 'e_o_k': [1.046545, 0.837236, 0.669788], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.225789, 'e_o_k': [0.046268, 0.037015, 0.029612], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 10.028404, 'e_o_k': [2.055001, 1.644001, 1.315201], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 5.390837, 'e_o_k': [1.104680, 0.883744, 0.706995], 'p_i': 40, 'u_i': 3.9189},
        {'id': 6, 'e_m': 0.266387, 'e_o_k': [0.054588, 0.043670, 0.034936], 'p_i': 10, 'u_i': 2.1344},
        {'id': 7, 'e_m': 4.383523, 'e_o_k': [0.898263, 0.718610, 0.574888], 'p_i': 40, 'u_i': 2.5225},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
