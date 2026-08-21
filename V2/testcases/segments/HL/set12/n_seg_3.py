"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399977, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399977, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.147016, 'e_o_k': [0.235044, 0.188035, 0.150428], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 3.773755, 'e_o_k': [0.773311, 0.618648, 0.494919], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 5.350477, 'e_o_k': [1.096409, 0.877127, 0.701702], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 16.969247, 'e_o_k': [3.477305, 2.781844, 2.225475], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 1.099497, 'e_o_k': [0.225307, 0.180245, 0.144196], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.148964, 'e_o_k': [0.030525, 0.024420, 0.019536], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 3.297912, 'e_o_k': [0.675802, 0.540641, 0.432513], 'p_i': 80, 'u_i': 2.9271},
        {'id': 7, 'e_m': 3.766890, 'e_o_k': [0.771904, 0.617523, 0.494018], 'p_i': 80, 'u_i': 1.9023},
    ]
    B_BUDGET = 110.399977
    return processors, tasks, B_BUDGET
