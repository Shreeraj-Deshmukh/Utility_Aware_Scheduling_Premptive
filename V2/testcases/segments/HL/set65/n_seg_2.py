"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127808, 'e_o_k': [0.035502, 0.028402], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 4.638287, 'e_o_k': [1.288413, 1.030730], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.800790, 'e_o_k': [0.222442, 0.177953], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 9.437860, 'e_o_k': [2.621628, 2.097302], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 3.483129, 'e_o_k': [0.967536, 0.774029], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 14.523637, 'e_o_k': [4.034343, 3.227475], 'p_i': 80, 'u_i': 4.6158},
        {'id': 6, 'e_m': 0.073356, 'e_o_k': [0.020377, 0.016301], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 1.158844, 'e_o_k': [0.321901, 0.257521], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET
