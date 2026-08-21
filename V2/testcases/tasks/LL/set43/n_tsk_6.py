"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.036102, 'e_o_k': [0.007398, 0.005918, 0.004735], 'p_i': 10, 'u_i': 4.0506},
        {'id': 1, 'e_m': 1.771436, 'e_o_k': [0.362999, 0.290399, 0.232319], 'p_i': 20, 'u_i': 2.8657},
        {'id': 2, 'e_m': 2.727861, 'e_o_k': [0.462036, 0.369629, 0.295703, 0.236562], 'p_i': 40, 'u_i': 2.1758},
        {'id': 3, 'e_m': 3.290322, 'e_o_k': [0.913978, 0.731183], 'p_i': 80, 'u_i': 2.5351},
        {'id': 4, 'e_m': 0.843218, 'e_o_k': [0.142821, 0.114257, 0.091406, 0.073125], 'p_i': 40, 'u_i': 3.6072},
        {'id': 5, 'e_m': 7.096482, 'e_o_k': [0.961771, 0.769416, 0.615533, 0.492427, 0.393941, 0.315153], 'p_i': 40, 'u_i': 4.5999},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
