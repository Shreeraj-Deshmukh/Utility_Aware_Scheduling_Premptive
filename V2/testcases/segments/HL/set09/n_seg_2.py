"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.737228, 'e_o_k': [0.482563, 0.386051], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 1.414064, 'e_o_k': [0.392796, 0.314236], 'p_i': 20, 'u_i': 3.6949},
        {'id': 2, 'e_m': 8.894962, 'e_o_k': [2.470823, 1.976658], 'p_i': 40, 'u_i': 3.0423},
        {'id': 3, 'e_m': 3.992321, 'e_o_k': [1.108978, 0.887182], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.156022, 'e_o_k': [0.043339, 0.034671], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.352177, 'e_o_k': [0.097827, 0.078262], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 5.127088, 'e_o_k': [1.424191, 1.139353], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 1.297088, 'e_o_k': [0.360302, 0.288242], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
