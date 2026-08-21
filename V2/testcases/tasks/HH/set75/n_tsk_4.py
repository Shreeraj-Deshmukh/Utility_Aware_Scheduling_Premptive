"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.589869, 'e_o_k': [0.754003, 0.603202, 0.482562, 0.386049], 'p_i': 10, 'u_i': 2.2754},
        {'id': 1, 'e_m': 2.051152, 'e_o_k': [1.595340, 1.276272], 'p_i': 20, 'u_i': 1.2102},
        {'id': 2, 'e_m': 9.003988, 'e_o_k': [5.166222, 4.132978, 3.306382], 'p_i': 40, 'u_i': 3.7306},
        {'id': 3, 'e_m': 25.068465, 'e_o_k': [14.383546, 11.506836, 9.205469], 'p_i': 80, 'u_i': 4.1325},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
