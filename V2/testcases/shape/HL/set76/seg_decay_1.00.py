"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399967, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399967, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.094835, 'e_o_k': [0.136854, 0.136854, 0.136854, 0.136854], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 6.015361, 'e_o_k': [1.002560, 1.002560, 1.002560], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 1.364859, 'e_o_k': [0.113738, 0.113738, 0.113738, 0.113738, 0.113738, 0.113738], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 1.209297, 'e_o_k': [0.201550, 0.201550, 0.201550], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 2.498208, 'e_o_k': [0.312276, 0.312276, 0.312276, 0.312276], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.889705, 'e_o_k': [0.148284, 0.148284, 0.148284], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.376895, 'e_o_k': [0.094224, 0.094224], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 5.337019, 'e_o_k': [1.334255, 1.334255], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 110.399967
    return processors, tasks, B_BUDGET
