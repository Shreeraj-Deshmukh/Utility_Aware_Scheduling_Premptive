"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.015283, 'e_o_k': [0.282023, 0.225618], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 1.338137, 'e_o_k': [0.371705, 0.297364], 'p_i': 20, 'u_i': 2.0395},
        {'id': 2, 'e_m': 1.215369, 'e_o_k': [0.337603, 0.270082], 'p_i': 40, 'u_i': 3.8865},
        {'id': 3, 'e_m': 11.427473, 'e_o_k': [3.174298, 2.539438], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 4.192750, 'e_o_k': [1.164653, 0.931722], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.541048, 'e_o_k': [0.150291, 0.120233], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 5.660701, 'e_o_k': [1.572417, 1.257934], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.655144, 'e_o_k': [0.181984, 0.145588], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
