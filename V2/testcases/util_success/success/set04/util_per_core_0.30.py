"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760002, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760002, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.697317, 'e_o_k': [0.056703, 0.045363, 0.036290, 0.029032, 0.023226, 0.018581], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.042658, 'e_o_k': [0.003469, 0.002775, 0.002220, 0.001776, 0.001421, 0.001137], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 1.967995, 'e_o_k': [0.327999, 0.262399], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 3.356005, 'e_o_k': [0.559334, 0.447467], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 1.762251, 'e_o_k': [0.293709, 0.234967], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 7.907241, 'e_o_k': [0.803581, 0.642865, 0.514292, 0.411434], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.256842, 'e_o_k': [0.042807, 0.034246], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 2.510153, 'e_o_k': [0.418359, 0.334687], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 71.760002
    return processors, tasks, B_BUDGET
