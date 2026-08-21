"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.744800, 'e_o_k': [0.282635, 0.226108, 0.180887, 0.144709, 0.115767, 0.092614], 'p_i': 10, 'u_i': 3.7891},
        {'id': 1, 'e_m': 3.749675, 'e_o_k': [2.151453, 1.721162, 1.376930], 'p_i': 20, 'u_i': 1.3517},
        {'id': 2, 'e_m': 0.781902, 'e_o_k': [0.370821, 0.296656, 0.237325, 0.189860], 'p_i': 40, 'u_i': 4.0093},
        {'id': 3, 'e_m': 0.788707, 'e_o_k': [0.452537, 0.362030, 0.289624], 'p_i': 80, 'u_i': 1.1110},
        {'id': 4, 'e_m': 6.484443, 'e_o_k': [2.460702, 1.968562, 1.574849, 1.259880, 1.007904, 0.806323], 'p_i': 80, 'u_i': 1.1701},
        {'id': 5, 'e_m': 0.551486, 'e_o_k': [0.316427, 0.253141, 0.202513], 'p_i': 20, 'u_i': 4.4848},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
