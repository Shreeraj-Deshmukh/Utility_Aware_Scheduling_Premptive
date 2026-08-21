"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.701313, 'e_o_k': [0.194809, 0.155847], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 6.860890, 'e_o_k': [1.905803, 1.524642], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.414599, 'e_o_k': [0.115166, 0.092133], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 3.429684, 'e_o_k': [0.952690, 0.762152], 'p_i': 80, 'u_i': 2.5958},
        {'id': 4, 'e_m': 1.398858, 'e_o_k': [0.388572, 0.310857], 'p_i': 20, 'u_i': 1.3643},
        {'id': 5, 'e_m': 5.494678, 'e_o_k': [1.526299, 1.221039], 'p_i': 80, 'u_i': 4.2904},
        {'id': 6, 'e_m': 5.102592, 'e_o_k': [1.417387, 1.133909], 'p_i': 40, 'u_i': 4.4714},
        {'id': 7, 'e_m': 5.391763, 'e_o_k': [1.497712, 1.198170], 'p_i': 80, 'u_i': 4.7028},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
