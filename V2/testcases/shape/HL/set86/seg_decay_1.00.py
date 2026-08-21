"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100443, 'e_o_k': [0.016741, 0.016741, 0.016741], 'p_i': 10, 'u_i': 2.4144},
        {'id': 1, 'e_m': 0.413851, 'e_o_k': [0.103463, 0.103463], 'p_i': 20, 'u_i': 2.6559},
        {'id': 2, 'e_m': 2.380758, 'e_o_k': [0.238076, 0.238076, 0.238076, 0.238076, 0.238076], 'p_i': 40, 'u_i': 2.8681},
        {'id': 3, 'e_m': 13.943895, 'e_o_k': [3.485974, 3.485974], 'p_i': 80, 'u_i': 1.8896},
        {'id': 4, 'e_m': 1.101724, 'e_o_k': [0.110172, 0.110172, 0.110172, 0.110172, 0.110172], 'p_i': 20, 'u_i': 1.6645},
        {'id': 5, 'e_m': 0.583734, 'e_o_k': [0.058373, 0.058373, 0.058373, 0.058373, 0.058373], 'p_i': 40, 'u_i': 1.3774},
        {'id': 6, 'e_m': 3.223359, 'e_o_k': [0.805840, 0.805840], 'p_i': 80, 'u_i': 1.9412},
        {'id': 7, 'e_m': 34.037914, 'e_o_k': [8.509478, 8.509478], 'p_i': 80, 'u_i': 2.2237},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
