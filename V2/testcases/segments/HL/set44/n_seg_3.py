"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.253914, 'e_o_k': [0.052032, 0.041625, 0.033300], 'p_i': 10, 'u_i': 1.1447},
        {'id': 1, 'e_m': 2.444497, 'e_o_k': [0.500921, 0.400737, 0.320590], 'p_i': 20, 'u_i': 4.1970},
        {'id': 2, 'e_m': 1.438401, 'e_o_k': [0.294754, 0.235804, 0.188643], 'p_i': 40, 'u_i': 2.1490},
        {'id': 3, 'e_m': 9.006906, 'e_o_k': [1.845677, 1.476542, 1.181234], 'p_i': 80, 'u_i': 1.5069},
        {'id': 4, 'e_m': 0.947423, 'e_o_k': [0.194144, 0.155315, 0.124252], 'p_i': 20, 'u_i': 3.9372},
        {'id': 5, 'e_m': 0.973099, 'e_o_k': [0.199406, 0.159524, 0.127620], 'p_i': 20, 'u_i': 1.6580},
        {'id': 6, 'e_m': 1.046300, 'e_o_k': [0.214406, 0.171525, 0.137220], 'p_i': 20, 'u_i': 4.1894},
        {'id': 7, 'e_m': 28.439701, 'e_o_k': [5.827808, 4.662246, 3.729797], 'p_i': 80, 'u_i': 4.9102},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
