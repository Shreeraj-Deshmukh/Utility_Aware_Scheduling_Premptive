"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.661670, 'e_o_k': [0.692033, 0.553626, 0.442901, 0.354321, 0.283457], 'p_i': 10, 'u_i': 3.1570},
        {'id': 1, 'e_m': 5.070765, 'e_o_k': [2.111813, 1.689451, 1.351560, 1.081248, 0.864999], 'p_i': 20, 'u_i': 1.1037},
        {'id': 2, 'e_m': 4.227938, 'e_o_k': [2.005120, 1.604096, 1.283277, 1.026621], 'p_i': 40, 'u_i': 1.2642},
        {'id': 3, 'e_m': 21.967705, 'e_o_k': [8.336257, 6.669006, 5.335205, 4.268164, 3.414531, 2.731625], 'p_i': 80, 'u_i': 2.8053},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET
