"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.659774, 'e_o_k': [1.016604, 0.813283], 'p_i': 10, 'u_i': 4.8131},
        {'id': 1, 'e_m': 3.615342, 'e_o_k': [0.537741, 0.430193, 0.344154, 0.275324, 0.220259], 'p_i': 20, 'u_i': 1.8577},
        {'id': 2, 'e_m': 2.245523, 'e_o_k': [0.460148, 0.368119, 0.294495], 'p_i': 40, 'u_i': 4.0468},
        {'id': 3, 'e_m': 3.223826, 'e_o_k': [0.479508, 0.383606, 0.306885, 0.245508, 0.196406], 'p_i': 80, 'u_i': 2.5682},
        {'id': 4, 'e_m': 9.283514, 'e_o_k': [1.258174, 1.006539, 0.805231, 0.644185, 0.515348, 0.412279], 'p_i': 80, 'u_i': 1.7800},
        {'id': 5, 'e_m': 0.407757, 'e_o_k': [0.055262, 0.044210, 0.035368, 0.028294, 0.022635, 0.018108], 'p_i': 10, 'u_i': 2.6825},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET
