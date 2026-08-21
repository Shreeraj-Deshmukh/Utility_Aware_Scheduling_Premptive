"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 32, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 32, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.711602, 'e_o_k': [0.553468, 0.442774], 'p_i': 10, 'u_i': 2.7633},
        {'id': 1, 'e_m': 1.956038, 'e_o_k': [0.742273, 0.593819, 0.475055, 0.380044, 0.304035, 0.243228], 'p_i': 20, 'u_i': 3.1688},
        {'id': 2, 'e_m': 6.578908, 'e_o_k': [3.774783, 3.019827, 2.415861], 'p_i': 40, 'u_i': 3.7705},
        {'id': 3, 'e_m': 14.898312, 'e_o_k': [8.548212, 6.838569, 5.470855], 'p_i': 80, 'u_i': 2.4357},
        {'id': 4, 'e_m': 4.819102, 'e_o_k': [2.285482, 1.828386, 1.462708, 1.170167], 'p_i': 80, 'u_i': 1.7399},
        {'id': 5, 'e_m': 0.459436, 'e_o_k': [0.174346, 0.139477, 0.111581, 0.089265, 0.071412, 0.057130], 'p_i': 10, 'u_i': 4.3140},
        {'id': 6, 'e_m': 1.319662, 'e_o_k': [0.549598, 0.439678, 0.351742, 0.281394, 0.225115], 'p_i': 20, 'u_i': 3.3669},
        {'id': 7, 'e_m': 2.163416, 'e_o_k': [1.682657, 1.346125], 'p_i': 20, 'u_i': 1.8038},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
