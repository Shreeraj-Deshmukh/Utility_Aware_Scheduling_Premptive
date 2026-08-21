"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.201315, 'e_o_k': [0.656007, 0.524806, 0.419845], 'p_i': 10, 'u_i': 1.6704},
        {'id': 1, 'e_m': 2.963590, 'e_o_k': [0.440801, 0.352640, 0.282112, 0.225690, 0.180552], 'p_i': 20, 'u_i': 3.6515},
        {'id': 2, 'e_m': 3.000662, 'e_o_k': [0.508242, 0.406594, 0.325275, 0.260220], 'p_i': 40, 'u_i': 1.3011},
        {'id': 3, 'e_m': 20.533791, 'e_o_k': [3.477946, 2.782357, 2.225885, 1.780708], 'p_i': 80, 'u_i': 4.8603},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
