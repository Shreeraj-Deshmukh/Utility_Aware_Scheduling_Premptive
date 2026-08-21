"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.900798, 'e_o_k': [0.527999, 0.422399], 'p_i': 10, 'u_i': 1.8275},
        {'id': 1, 'e_m': 3.986843, 'e_o_k': [1.107456, 0.885965], 'p_i': 20, 'u_i': 3.9821},
        {'id': 2, 'e_m': 16.273710, 'e_o_k': [2.205540, 1.764432, 1.411546, 1.129237, 0.903389, 0.722711], 'p_i': 40, 'u_i': 4.4924},
        {'id': 3, 'e_m': 0.298826, 'e_o_k': [0.061235, 0.048988, 0.039190], 'p_i': 80, 'u_i': 4.2054},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET
