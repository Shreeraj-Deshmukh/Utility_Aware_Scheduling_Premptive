"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400013, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400013, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127808, 'e_o_k': [0.026190, 0.020952, 0.016762], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 4.638287, 'e_o_k': [0.950469, 0.760375, 0.608300], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.800790, 'e_o_k': [0.164096, 0.131277, 0.105022], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 9.437860, 'e_o_k': [1.933988, 1.547190, 1.237752], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 3.483129, 'e_o_k': [0.713756, 0.571005, 0.456804], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 14.523637, 'e_o_k': [2.976155, 2.380924, 1.904739], 'p_i': 80, 'u_i': 4.6158},
        {'id': 6, 'e_m': 0.073356, 'e_o_k': [0.015032, 0.012026, 0.009620], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 1.158844, 'e_o_k': [0.237468, 0.189974, 0.151980], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 110.400013
    return processors, tasks, B_BUDGET
