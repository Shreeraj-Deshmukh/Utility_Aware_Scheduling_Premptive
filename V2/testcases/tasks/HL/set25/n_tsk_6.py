"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.145778, 'e_o_k': [0.319160, 0.255328, 0.204263, 0.163410, 0.130728], 'p_i': 10, 'u_i': 4.5978},
        {'id': 1, 'e_m': 6.335860, 'e_o_k': [1.298332, 1.038666, 0.830933], 'p_i': 20, 'u_i': 3.9895},
        {'id': 2, 'e_m': 3.211158, 'e_o_k': [0.891988, 0.713591], 'p_i': 40, 'u_i': 3.6989},
        {'id': 3, 'e_m': 7.854319, 'e_o_k': [1.330339, 1.064271, 0.851417, 0.681133], 'p_i': 80, 'u_i': 3.2467},
        {'id': 4, 'e_m': 2.331101, 'e_o_k': [0.477685, 0.382148, 0.305718], 'p_i': 80, 'u_i': 4.5958},
        {'id': 5, 'e_m': 2.441297, 'e_o_k': [0.413499, 0.330799, 0.264639, 0.211711], 'p_i': 40, 'u_i': 4.0042},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
