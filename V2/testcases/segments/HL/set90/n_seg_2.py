"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.855925, 'e_o_k': [0.237757, 0.190205], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 2.062245, 'e_o_k': [0.572846, 0.458277], 'p_i': 20, 'u_i': 3.8670},
        {'id': 2, 'e_m': 1.796246, 'e_o_k': [0.498957, 0.399166], 'p_i': 40, 'u_i': 1.6834},
        {'id': 3, 'e_m': 0.729094, 'e_o_k': [0.202526, 0.162021], 'p_i': 80, 'u_i': 3.8684},
        {'id': 4, 'e_m': 2.221698, 'e_o_k': [0.617138, 0.493711], 'p_i': 40, 'u_i': 4.7513},
        {'id': 5, 'e_m': 13.925733, 'e_o_k': [3.868259, 3.094607], 'p_i': 40, 'u_i': 4.4932},
        {'id': 6, 'e_m': 5.950860, 'e_o_k': [1.653017, 1.322413], 'p_i': 40, 'u_i': 1.6064},
        {'id': 7, 'e_m': 0.048181, 'e_o_k': [0.013384, 0.010707], 'p_i': 10, 'u_i': 2.2133},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
