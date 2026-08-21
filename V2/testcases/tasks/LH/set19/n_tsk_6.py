"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.962850, 'e_o_k': [0.817465, 0.653972, 0.523177, 0.418542, 0.334834], 'p_i': 10, 'u_i': 2.5478},
        {'id': 1, 'e_m': 1.302586, 'e_o_k': [0.617758, 0.494206, 0.395365, 0.316292], 'p_i': 20, 'u_i': 1.9017},
        {'id': 2, 'e_m': 0.446219, 'e_o_k': [0.347059, 0.277647], 'p_i': 40, 'u_i': 4.1004},
        {'id': 3, 'e_m': 3.381996, 'e_o_k': [1.603928, 1.283142, 1.026514, 0.821211], 'p_i': 80, 'u_i': 2.6358},
        {'id': 4, 'e_m': 0.023935, 'e_o_k': [0.013733, 0.010986, 0.008789], 'p_i': 20, 'u_i': 4.3577},
        {'id': 5, 'e_m': 3.358343, 'e_o_k': [1.592710, 1.274168, 1.019334, 0.815468], 'p_i': 40, 'u_i': 4.2383},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
