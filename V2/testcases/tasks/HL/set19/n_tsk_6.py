"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.925700, 'e_o_k': [0.583903, 0.467123, 0.373698, 0.298959, 0.239167], 'p_i': 10, 'u_i': 2.5478},
        {'id': 1, 'e_m': 2.605172, 'e_o_k': [0.441255, 0.353004, 0.282403, 0.225923], 'p_i': 20, 'u_i': 1.9017},
        {'id': 2, 'e_m': 0.892438, 'e_o_k': [0.247899, 0.198320], 'p_i': 40, 'u_i': 4.1004},
        {'id': 3, 'e_m': 6.763993, 'e_o_k': [1.145663, 0.916530, 0.733224, 0.586579], 'p_i': 80, 'u_i': 2.6358},
        {'id': 4, 'e_m': 0.047869, 'e_o_k': [0.009809, 0.007847, 0.006278], 'p_i': 20, 'u_i': 4.3577},
        {'id': 5, 'e_m': 6.716685, 'e_o_k': [1.137650, 0.910120, 0.728096, 0.582477], 'p_i': 40, 'u_i': 4.2383},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
