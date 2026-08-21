"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119979, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119979, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.583486, 'e_o_k': [0.465801, 0.372641, 0.298113, 0.238490], 'p_i': 10, 'u_i': 2.5191},
        {'id': 1, 'e_m': 1.595950, 'e_o_k': [0.129777, 0.103822, 0.083058, 0.066446, 0.053157, 0.042525], 'p_i': 20, 'u_i': 1.4276},
        {'id': 2, 'e_m': 5.032955, 'e_o_k': [0.449157, 0.359326, 0.287461, 0.229968, 0.183975], 'p_i': 40, 'u_i': 2.4044},
        {'id': 3, 'e_m': 14.238388, 'e_o_k': [1.446991, 1.157593, 0.926074, 0.740859], 'p_i': 80, 'u_i': 3.6414},
        {'id': 4, 'e_m': 4.244431, 'e_o_k': [0.378787, 0.303029, 0.242423, 0.193939, 0.155151], 'p_i': 20, 'u_i': 3.1817},
        {'id': 5, 'e_m': 3.903265, 'e_o_k': [0.650544, 0.520435], 'p_i': 10, 'u_i': 1.8252},
        {'id': 6, 'e_m': 12.639791, 'e_o_k': [1.554073, 1.243258, 0.994607], 'p_i': 40, 'u_i': 3.6022},
        {'id': 7, 'e_m': 35.160581, 'e_o_k': [5.860097, 4.688077], 'p_i': 80, 'u_i': 2.1719},
    ]
    B_BUDGET = 263.119979
    return processors, tasks, B_BUDGET
