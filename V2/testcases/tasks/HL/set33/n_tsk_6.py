"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.067388, 'e_o_k': [0.018719, 0.014975], 'p_i': 10, 'u_i': 2.5143},
        {'id': 1, 'e_m': 5.132687, 'e_o_k': [0.763429, 0.610743, 0.488595, 0.390876, 0.312701], 'p_i': 20, 'u_i': 1.6130},
        {'id': 2, 'e_m': 7.548845, 'e_o_k': [1.546894, 1.237516, 0.990012], 'p_i': 40, 'u_i': 1.3758},
        {'id': 3, 'e_m': 1.400496, 'e_o_k': [0.286987, 0.229589, 0.183672], 'p_i': 80, 'u_i': 3.6848},
        {'id': 4, 'e_m': 3.078148, 'e_o_k': [0.855041, 0.684033], 'p_i': 10, 'u_i': 1.6851},
        {'id': 5, 'e_m': 0.451694, 'e_o_k': [0.067184, 0.053747, 0.042998, 0.034398, 0.027519], 'p_i': 20, 'u_i': 1.3700},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET
