"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400012, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400012, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.691442, 'e_o_k': [0.141689, 0.113351, 0.090681], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 3.651177, 'e_o_k': [0.748192, 0.598554, 0.478843], 'p_i': 20, 'u_i': 2.2851},
        {'id': 2, 'e_m': 5.369710, 'e_o_k': [1.100350, 0.880280, 0.704224], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 9.653701, 'e_o_k': [1.978217, 1.582574, 1.266059], 'p_i': 80, 'u_i': 2.3867},
        {'id': 4, 'e_m': 0.756812, 'e_o_k': [0.155085, 0.124068, 0.099254], 'p_i': 10, 'u_i': 1.9527},
        {'id': 5, 'e_m': 0.749641, 'e_o_k': [0.153615, 0.122892, 0.098314], 'p_i': 10, 'u_i': 2.5555},
        {'id': 6, 'e_m': 6.748626, 'e_o_k': [1.382915, 1.106332, 0.885066], 'p_i': 80, 'u_i': 2.5749},
        {'id': 7, 'e_m': 2.335192, 'e_o_k': [0.478523, 0.382818, 0.306255], 'p_i': 40, 'u_i': 4.5972},
    ]
    B_BUDGET = 110.400012
    return processors, tasks, B_BUDGET
