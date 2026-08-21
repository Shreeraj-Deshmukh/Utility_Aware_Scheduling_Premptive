"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.498114, 'e_o_k': [0.387422, 0.309938], 'p_i': 10, 'u_i': 2.6429},
        {'id': 1, 'e_m': 0.521769, 'e_o_k': [0.217300, 0.173840, 0.139072, 0.111258, 0.089006], 'p_i': 20, 'u_i': 1.6574},
        {'id': 2, 'e_m': 9.762141, 'e_o_k': [4.065623, 3.252498, 2.601998, 2.081599, 1.665279], 'p_i': 40, 'u_i': 4.4970},
        {'id': 3, 'e_m': 6.403733, 'e_o_k': [3.674273, 2.939418, 2.351535], 'p_i': 80, 'u_i': 1.4275},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
