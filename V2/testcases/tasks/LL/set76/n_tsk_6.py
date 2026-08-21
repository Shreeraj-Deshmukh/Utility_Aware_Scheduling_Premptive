"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.744800, 'e_o_k': [0.100941, 0.080753, 0.064602, 0.051682, 0.041345, 0.033076], 'p_i': 10, 'u_i': 3.7891},
        {'id': 1, 'e_m': 3.749675, 'e_o_k': [0.768376, 0.614701, 0.491761], 'p_i': 20, 'u_i': 1.3517},
        {'id': 2, 'e_m': 0.781902, 'e_o_k': [0.132436, 0.105949, 0.084759, 0.067807], 'p_i': 40, 'u_i': 4.0093},
        {'id': 3, 'e_m': 0.788707, 'e_o_k': [0.161620, 0.129296, 0.103437], 'p_i': 80, 'u_i': 1.1110},
        {'id': 4, 'e_m': 6.484443, 'e_o_k': [0.878822, 0.703058, 0.562446, 0.449957, 0.359966, 0.287972], 'p_i': 80, 'u_i': 1.1701},
        {'id': 5, 'e_m': 0.551486, 'e_o_k': [0.113010, 0.090408, 0.072326], 'p_i': 20, 'u_i': 4.4848},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET
