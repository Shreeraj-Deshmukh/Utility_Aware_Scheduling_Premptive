"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.689807, 'e_o_k': [0.168981, 0.168981, 0.168981, 0.168981, 0.168981], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.355169, 'e_o_k': [0.088792, 0.088792], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 2.867086, 'e_o_k': [0.358386, 0.358386, 0.358386, 0.358386], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 3.497724, 'e_o_k': [0.874431, 0.874431], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 13.830064, 'e_o_k': [1.152505, 1.152505, 1.152505, 1.152505, 1.152505, 1.152505], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 3.101531, 'e_o_k': [0.387691, 0.387691, 0.387691, 0.387691], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.222281, 'e_o_k': [0.055570, 0.055570], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 2.953634, 'e_o_k': [0.246136, 0.246136, 0.246136, 0.246136, 0.246136, 0.246136], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
