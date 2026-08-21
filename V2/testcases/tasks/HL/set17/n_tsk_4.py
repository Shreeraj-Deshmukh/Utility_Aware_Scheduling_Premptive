"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.730494, 'e_o_k': [0.480693, 0.384554], 'p_i': 10, 'u_i': 2.4127},
        {'id': 1, 'e_m': 2.545488, 'e_o_k': [0.707080, 0.565664], 'p_i': 20, 'u_i': 2.1691},
        {'id': 2, 'e_m': 16.173972, 'e_o_k': [4.492770, 3.594216], 'p_i': 40, 'u_i': 3.6581},
        {'id': 3, 'e_m': 7.626156, 'e_o_k': [1.134305, 0.907444, 0.725955, 0.580764, 0.464611], 'p_i': 80, 'u_i': 4.4037},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET
