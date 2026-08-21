"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.484964, 'e_o_k': [0.134712, 0.107770], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.736640, 'e_o_k': [0.204622, 0.163698], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 4.567615, 'e_o_k': [1.268782, 1.015026], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 2.590483, 'e_o_k': [0.719579, 0.575663], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 1.196360, 'e_o_k': [0.332322, 0.265858], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 5.644234, 'e_o_k': [1.567843, 1.254274], 'p_i': 40, 'u_i': 1.9356},
        {'id': 6, 'e_m': 25.995886, 'e_o_k': [7.221079, 5.776864], 'p_i': 80, 'u_i': 1.5831},
        {'id': 7, 'e_m': 3.483648, 'e_o_k': [0.967680, 0.774144], 'p_i': 40, 'u_i': 3.6851},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET
