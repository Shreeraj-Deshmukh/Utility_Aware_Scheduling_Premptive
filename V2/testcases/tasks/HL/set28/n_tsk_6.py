"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.143043, 'e_o_k': [0.154914, 0.123931, 0.099145, 0.079316, 0.063453, 0.050762], 'p_i': 10, 'u_i': 2.5404},
        {'id': 1, 'e_m': 2.851808, 'e_o_k': [0.584387, 0.467509, 0.374008], 'p_i': 20, 'u_i': 1.0986},
        {'id': 2, 'e_m': 3.105701, 'e_o_k': [0.862695, 0.690156], 'p_i': 40, 'u_i': 3.7025},
        {'id': 3, 'e_m': 18.529161, 'e_o_k': [5.146989, 4.117591], 'p_i': 80, 'u_i': 4.4926},
        {'id': 4, 'e_m': 1.923092, 'e_o_k': [0.394076, 0.315261, 0.252209], 'p_i': 80, 'u_i': 3.2922},
        {'id': 5, 'e_m': 8.392386, 'e_o_k': [2.331218, 1.864975], 'p_i': 40, 'u_i': 3.7450},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET
