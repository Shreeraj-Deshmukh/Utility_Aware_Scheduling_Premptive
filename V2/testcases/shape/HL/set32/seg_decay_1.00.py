"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399976, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399976, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.015283, 'e_o_k': [0.101528, 0.101528, 0.101528, 0.101528, 0.101528], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 1.338137, 'e_o_k': [0.111511, 0.111511, 0.111511, 0.111511, 0.111511, 0.111511], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 1.215369, 'e_o_k': [0.101281, 0.101281, 0.101281, 0.101281, 0.101281, 0.101281], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 11.427473, 'e_o_k': [2.856868, 2.856868], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 4.192750, 'e_o_k': [0.524094, 0.524094, 0.524094, 0.524094], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.541048, 'e_o_k': [0.067631, 0.067631, 0.067631, 0.067631], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 5.660701, 'e_o_k': [1.415175, 1.415175], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.655144, 'e_o_k': [0.163786, 0.163786], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 110.399976
    return processors, tasks, B_BUDGET
