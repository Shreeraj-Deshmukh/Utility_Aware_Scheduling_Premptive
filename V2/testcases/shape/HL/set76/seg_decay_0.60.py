"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399984, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399984, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.094835, 'e_o_k': [0.251571, 0.150942, 0.090565, 0.054339], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 6.015361, 'e_o_k': [1.534531, 0.920719, 0.552431], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 1.364859, 'e_o_k': [0.286331, 0.171799, 0.103079, 0.061847, 0.037108, 0.022265], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 1.209297, 'e_o_k': [0.308494, 0.185097, 0.111058], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 2.498208, 'e_o_k': [0.574037, 0.344422, 0.206653, 0.123992], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.889705, 'e_o_k': [0.226966, 0.136179, 0.081708], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.376895, 'e_o_k': [0.117780, 0.070668], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 5.337019, 'e_o_k': [1.667818, 1.000691], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 110.399984
    return processors, tasks, B_BUDGET
