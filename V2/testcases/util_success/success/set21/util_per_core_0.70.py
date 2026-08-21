"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.210024, 'e_o_k': [0.148773, 0.119019, 0.095215], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 6.389560, 'e_o_k': [0.519578, 0.415662, 0.332530, 0.266024, 0.212819, 0.170255], 'p_i': 20, 'u_i': 1.0830},
        {'id': 2, 'e_m': 9.396992, 'e_o_k': [1.566165, 1.252932], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 16.893976, 'e_o_k': [1.373762, 1.099010, 0.879208, 0.703366, 0.562693, 0.450154], 'p_i': 80, 'u_i': 2.8864},
        {'id': 4, 'e_m': 1.324422, 'e_o_k': [0.118196, 0.094557, 0.075645, 0.060516, 0.048413], 'p_i': 10, 'u_i': 1.3892},
        {'id': 5, 'e_m': 1.311871, 'e_o_k': [0.133320, 0.106656, 0.085325, 0.068260], 'p_i': 10, 'u_i': 2.4866},
        {'id': 6, 'e_m': 11.810096, 'e_o_k': [1.053971, 0.843177, 0.674541, 0.539633, 0.431706], 'p_i': 80, 'u_i': 4.5153},
        {'id': 7, 'e_m': 4.086586, 'e_o_k': [0.364700, 0.291760, 0.233408, 0.186726, 0.149381], 'p_i': 40, 'u_i': 1.1207},
    ]
    B_BUDGET = 167.440001
    return processors, tasks, B_BUDGET
