"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.309825, 'e_o_k': [0.046083, 0.036866, 0.029493, 0.023594, 0.018876], 'p_i': 10, 'u_i': 3.6728},
        {'id': 1, 'e_m': 4.220170, 'e_o_k': [0.571950, 0.457560, 0.366048, 0.292839, 0.234271, 0.187417], 'p_i': 20, 'u_i': 2.1630},
        {'id': 2, 'e_m': 12.095490, 'e_o_k': [1.639275, 1.311420, 1.049136, 0.839309, 0.671447, 0.537158], 'p_i': 40, 'u_i': 4.2465},
        {'id': 3, 'e_m': 20.449741, 'e_o_k': [2.771508, 2.217207, 1.773765, 1.419012, 1.135210, 0.908168], 'p_i': 80, 'u_i': 1.5896},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
