"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.893774, 'e_o_k': [0.248270, 0.198616], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.002051, 'e_o_k': [0.000570, 0.000456], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 13.125199, 'e_o_k': [3.645888, 2.916711], 'p_i': 40, 'u_i': 2.6491},
        {'id': 3, 'e_m': 4.683481, 'e_o_k': [1.300967, 1.040774], 'p_i': 80, 'u_i': 3.7785},
        {'id': 4, 'e_m': 0.355356, 'e_o_k': [0.098710, 0.078968], 'p_i': 10, 'u_i': 2.0110},
        {'id': 5, 'e_m': 0.683705, 'e_o_k': [0.189918, 0.151935], 'p_i': 10, 'u_i': 2.7392},
        {'id': 6, 'e_m': 12.075953, 'e_o_k': [3.354432, 2.683545], 'p_i': 80, 'u_i': 4.5700},
        {'id': 7, 'e_m': 1.379822, 'e_o_k': [0.383284, 0.306627], 'p_i': 20, 'u_i': 2.3393},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
