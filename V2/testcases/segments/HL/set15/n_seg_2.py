"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.212074, 'e_o_k': [0.614465, 0.491572], 'p_i': 10, 'u_i': 4.4310},
        {'id': 1, 'e_m': 2.099648, 'e_o_k': [0.583236, 0.466588], 'p_i': 20, 'u_i': 4.5357},
        {'id': 2, 'e_m': 0.255502, 'e_o_k': [0.070973, 0.056778], 'p_i': 40, 'u_i': 3.5135},
        {'id': 3, 'e_m': 6.162213, 'e_o_k': [1.711726, 1.369381], 'p_i': 80, 'u_i': 3.8723},
        {'id': 4, 'e_m': 3.257255, 'e_o_k': [0.904793, 0.723834], 'p_i': 80, 'u_i': 1.1816},
        {'id': 5, 'e_m': 1.792700, 'e_o_k': [0.497972, 0.398378], 'p_i': 40, 'u_i': 3.3631},
        {'id': 6, 'e_m': 14.597411, 'e_o_k': [4.054837, 3.243869], 'p_i': 80, 'u_i': 2.0216},
        {'id': 7, 'e_m': 1.223941, 'e_o_k': [0.339984, 0.271987], 'p_i': 10, 'u_i': 3.3728},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
