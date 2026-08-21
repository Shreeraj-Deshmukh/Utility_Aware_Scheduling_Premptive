"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.106643, 'e_o_k': [0.307401, 0.245921], 'p_i': 10, 'u_i': 2.8789},
        {'id': 1, 'e_m': 3.625744, 'e_o_k': [0.742980, 0.594384, 0.475507], 'p_i': 20, 'u_i': 1.7162},
        {'id': 2, 'e_m': 0.770106, 'e_o_k': [0.213918, 0.171135], 'p_i': 40, 'u_i': 1.4626},
        {'id': 3, 'e_m': 39.103672, 'e_o_k': [10.862131, 8.689705], 'p_i': 80, 'u_i': 2.2690},
    ]
    B_BUDGET = 110.400007
    return processors, tasks, B_BUDGET
