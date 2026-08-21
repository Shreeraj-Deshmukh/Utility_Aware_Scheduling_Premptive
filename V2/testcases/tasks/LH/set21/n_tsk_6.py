"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.475493, 'e_o_k': [0.225505, 0.180404, 0.144323, 0.115458], 'p_i': 10, 'u_i': 1.4304},
        {'id': 1, 'e_m': 2.468602, 'e_o_k': [1.028095, 0.822476, 0.657981, 0.526384, 0.421108], 'p_i': 20, 'u_i': 2.0301},
        {'id': 2, 'e_m': 3.424018, 'e_o_k': [1.425995, 1.140796, 0.912637, 0.730110, 0.584088], 'p_i': 40, 'u_i': 4.4775},
        {'id': 3, 'e_m': 5.713174, 'e_o_k': [2.168023, 1.734418, 1.387535, 1.110028, 0.888022, 0.710418], 'p_i': 80, 'u_i': 1.0830},
        {'id': 4, 'e_m': 3.406818, 'e_o_k': [2.649747, 2.119798], 'p_i': 80, 'u_i': 1.9156},
        {'id': 5, 'e_m': 2.353620, 'e_o_k': [0.893146, 0.714517, 0.571614, 0.457291, 0.365833, 0.292666], 'p_i': 80, 'u_i': 2.8864},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
