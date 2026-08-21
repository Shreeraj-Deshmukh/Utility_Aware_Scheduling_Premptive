"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.722711, 'e_o_k': [0.653731, 0.522985, 0.418388, 0.334710, 0.267768, 0.214214], 'p_i': 10, 'u_i': 3.5509},
        {'id': 1, 'e_m': 0.629824, 'e_o_k': [0.298697, 0.238958, 0.191166, 0.152933], 'p_i': 20, 'u_i': 2.4298},
        {'id': 2, 'e_m': 11.031418, 'e_o_k': [6.329502, 5.063602, 4.050882], 'p_i': 40, 'u_i': 2.9531},
        {'id': 3, 'e_m': 25.636179, 'e_o_k': [9.728362, 7.782690, 6.226152, 4.980921, 3.984737, 3.187790], 'p_i': 80, 'u_i': 4.5727},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
