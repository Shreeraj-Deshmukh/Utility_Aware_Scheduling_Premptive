"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400012, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400012, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.245057, 'e_o_k': [0.033212, 0.026570, 0.021256, 0.017005, 0.013604, 0.010883], 'p_i': 10, 'u_i': 4.9047},
        {'id': 1, 'e_m': 0.839324, 'e_o_k': [0.171993, 0.137594, 0.110075], 'p_i': 20, 'u_i': 3.2321},
        {'id': 2, 'e_m': 4.678797, 'e_o_k': [0.695918, 0.556735, 0.445388, 0.356310, 0.285048], 'p_i': 40, 'u_i': 3.3144},
        {'id': 3, 'e_m': 2.870116, 'e_o_k': [0.388981, 0.311184, 0.248948, 0.199158, 0.159326, 0.127461], 'p_i': 80, 'u_i': 1.1307},
        {'id': 4, 'e_m': 3.001449, 'e_o_k': [0.446432, 0.357145, 0.285716, 0.228573, 0.182858], 'p_i': 20, 'u_i': 4.3260},
        {'id': 5, 'e_m': 8.612185, 'e_o_k': [1.764792, 1.411834, 1.129467], 'p_i': 20, 'u_i': 4.7000},
    ]
    B_BUDGET = 110.400012
    return processors, tasks, B_BUDGET
