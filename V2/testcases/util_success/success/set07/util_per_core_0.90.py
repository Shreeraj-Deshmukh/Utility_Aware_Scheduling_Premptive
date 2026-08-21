"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.282314, 'e_o_k': [0.185590, 0.148472, 0.118778, 0.095022, 0.076018, 0.060814], 'p_i': 10, 'u_i': 3.5703},
        {'id': 1, 'e_m': 7.045449, 'e_o_k': [0.716001, 0.572801, 0.458241, 0.366592], 'p_i': 20, 'u_i': 4.1664},
        {'id': 2, 'e_m': 1.301821, 'e_o_k': [0.105860, 0.084688, 0.067750, 0.054200, 0.043360, 0.034688], 'p_i': 40, 'u_i': 1.4904},
        {'id': 3, 'e_m': 25.441356, 'e_o_k': [2.270468, 1.816375, 1.453100, 1.162480, 0.929984], 'p_i': 80, 'u_i': 4.1413},
        {'id': 4, 'e_m': 4.705184, 'e_o_k': [0.478169, 0.382535, 0.306028, 0.244823], 'p_i': 10, 'u_i': 2.8602},
        {'id': 5, 'e_m': 1.045110, 'e_o_k': [0.128497, 0.102798, 0.082238], 'p_i': 20, 'u_i': 3.3364},
        {'id': 6, 'e_m': 2.179611, 'e_o_k': [0.363268, 0.290615], 'p_i': 20, 'u_i': 2.1410},
        {'id': 7, 'e_m': 9.487171, 'e_o_k': [0.771465, 0.617172, 0.493738, 0.394990, 0.315992, 0.252794], 'p_i': 40, 'u_i': 4.3280},
    ]
    B_BUDGET = 215.280001
    return processors, tasks, B_BUDGET
