"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399982, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399982, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.660725, 'e_o_k': [0.545230, 0.436184, 0.348947], 'p_i': 10, 'u_i': 2.7301},
        {'id': 1, 'e_m': 0.191668, 'e_o_k': [0.032464, 0.025971, 0.020777, 0.016622], 'p_i': 20, 'u_i': 2.9329},
        {'id': 2, 'e_m': 6.038206, 'e_o_k': [1.022731, 0.818185, 0.654548, 0.523638], 'p_i': 40, 'u_i': 4.3550},
        {'id': 3, 'e_m': 2.896544, 'e_o_k': [0.430828, 0.344663, 0.275730, 0.220584, 0.176467], 'p_i': 80, 'u_i': 2.2741},
        {'id': 4, 'e_m': 1.536590, 'e_o_k': [0.314875, 0.251900, 0.201520], 'p_i': 10, 'u_i': 2.5808},
        {'id': 5, 'e_m': 7.340925, 'e_o_k': [1.091880, 0.873504, 0.698803, 0.559042, 0.447234], 'p_i': 40, 'u_i': 4.5356},
    ]
    B_BUDGET = 110.399982
    return processors, tasks, B_BUDGET
