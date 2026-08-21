"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.60001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.60001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.140768, 'e_o_k': [0.017308, 0.013846, 0.011077], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 0.858610, 'e_o_k': [0.143102, 0.114481], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 2.715970, 'e_o_k': [0.452662, 0.362129], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 5.393625, 'e_o_k': [0.548133, 0.438506, 0.350805, 0.280644], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.475931, 'e_o_k': [0.048367, 0.038694, 0.030955, 0.024764], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 10.018277, 'e_o_k': [1.231755, 0.985404, 0.788323], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 2.742451, 'e_o_k': [0.278704, 0.222964, 0.178371, 0.142697], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 28.848513, 'e_o_k': [3.546948, 2.837559, 2.270047], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 119.600010
    return processors, tasks, B_BUDGET
