"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399968, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.399968, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.855925, 'e_o_k': [0.085592, 0.085592, 0.085592, 0.085592, 0.085592], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 2.062245, 'e_o_k': [0.171854, 0.171854, 0.171854, 0.171854, 0.171854, 0.171854], 'p_i': 20, 'u_i': 3.3367},
        {'id': 2, 'e_m': 1.796246, 'e_o_k': [0.299374, 0.299374, 0.299374], 'p_i': 40, 'u_i': 4.5472},
        {'id': 3, 'e_m': 0.729094, 'e_o_k': [0.091137, 0.091137, 0.091137, 0.091137], 'p_i': 80, 'u_i': 1.6834},
        {'id': 4, 'e_m': 2.221698, 'e_o_k': [0.555424, 0.555424], 'p_i': 40, 'u_i': 3.8684},
        {'id': 5, 'e_m': 13.925733, 'e_o_k': [3.481433, 3.481433], 'p_i': 40, 'u_i': 4.7513},
        {'id': 6, 'e_m': 5.950860, 'e_o_k': [0.495905, 0.495905, 0.495905, 0.495905, 0.495905, 0.495905], 'p_i': 40, 'u_i': 2.4512},
        {'id': 7, 'e_m': 0.048181, 'e_o_k': [0.012045, 0.012045], 'p_i': 10, 'u_i': 1.4858},
    ]
    B_BUDGET = 110.399968
    return processors, tasks, B_BUDGET
