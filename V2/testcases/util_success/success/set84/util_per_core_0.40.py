"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679991, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679991, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.484964, 'e_o_k': [0.043280, 0.034624, 0.027699, 0.022159, 0.017727], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.736640, 'e_o_k': [0.090571, 0.072456, 0.057965], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 4.567615, 'e_o_k': [0.464189, 0.371351, 0.297081, 0.237665], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 2.590483, 'e_o_k': [0.431747, 0.345398], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 1.196360, 'e_o_k': [0.121581, 0.097265, 0.077812, 0.062250], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 5.644234, 'e_o_k': [0.458970, 0.367176, 0.293741, 0.234993, 0.187994, 0.150395], 'p_i': 40, 'u_i': 3.8755},
        {'id': 6, 'e_m': 25.995886, 'e_o_k': [3.196216, 2.556972, 2.045578], 'p_i': 80, 'u_i': 3.4836},
        {'id': 7, 'e_m': 3.483648, 'e_o_k': [0.428317, 0.342654, 0.274123], 'p_i': 40, 'u_i': 4.1699},
    ]
    B_BUDGET = 95.679991
    return processors, tasks, B_BUDGET
