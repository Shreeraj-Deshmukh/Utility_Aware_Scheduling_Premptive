"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.908996, 'e_o_k': [1.211505, 0.969204, 0.775363, 0.620291, 0.496232], 'p_i': 10, 'u_i': 1.8764},
        {'id': 1, 'e_m': 0.104544, 'e_o_k': [0.039672, 0.031738, 0.025390, 0.020312, 0.016250, 0.013000], 'p_i': 20, 'u_i': 4.1968},
        {'id': 2, 'e_m': 1.907409, 'e_o_k': [0.794375, 0.635500, 0.508400, 0.406720, 0.325376], 'p_i': 40, 'u_i': 4.4928},
        {'id': 3, 'e_m': 4.495037, 'e_o_k': [1.705767, 1.364613, 1.091691, 0.873353, 0.698682, 0.558946], 'p_i': 80, 'u_i': 4.0915},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
