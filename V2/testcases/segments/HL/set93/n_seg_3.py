"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.145211, 'e_o_k': [0.234674, 0.187739, 0.150192], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 1.131105, 'e_o_k': [0.231784, 0.185427, 0.148342], 'p_i': 20, 'u_i': 4.7220},
        {'id': 2, 'e_m': 1.635759, 'e_o_k': [0.335197, 0.268157, 0.214526], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 10.249639, 'e_o_k': [2.100336, 1.680269, 1.344215], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 4.233912, 'e_o_k': [0.867605, 0.694084, 0.555267], 'p_i': 20, 'u_i': 3.9894},
        {'id': 5, 'e_m': 0.437464, 'e_o_k': [0.089644, 0.071715, 0.057372], 'p_i': 10, 'u_i': 1.1602},
        {'id': 6, 'e_m': 2.093940, 'e_o_k': [0.429086, 0.343269, 0.274615], 'p_i': 20, 'u_i': 4.5224},
        {'id': 7, 'e_m': 7.981619, 'e_o_k': [1.635578, 1.308462, 1.046770], 'p_i': 80, 'u_i': 3.6370},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET
