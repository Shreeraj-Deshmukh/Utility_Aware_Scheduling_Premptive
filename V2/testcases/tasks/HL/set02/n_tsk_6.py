"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.978192, 'e_o_k': [0.132572, 0.106058, 0.084846, 0.067877, 0.054302, 0.043441], 'p_i': 10, 'u_i': 1.1924},
        {'id': 1, 'e_m': 2.729673, 'e_o_k': [0.559359, 0.447487, 0.357990], 'p_i': 20, 'u_i': 4.9854},
        {'id': 2, 'e_m': 8.948325, 'e_o_k': [2.485646, 1.988517], 'p_i': 40, 'u_i': 2.6844},
        {'id': 3, 'e_m': 17.481868, 'e_o_k': [2.369279, 1.895423, 1.516339, 1.213071, 0.970457, 0.776365], 'p_i': 80, 'u_i': 3.2251},
        {'id': 4, 'e_m': 0.637135, 'e_o_k': [0.130560, 0.104448, 0.083559], 'p_i': 10, 'u_i': 4.0273},
        {'id': 5, 'e_m': 4.780173, 'e_o_k': [0.979544, 0.783635, 0.626908], 'p_i': 80, 'u_i': 2.2476},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET
