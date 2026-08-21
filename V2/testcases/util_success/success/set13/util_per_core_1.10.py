"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119998, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119998, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.396333, 'e_o_k': [0.213856, 0.171085, 0.136868, 0.109494, 0.087596], 'p_i': 10, 'u_i': 1.4156},
        {'id': 1, 'e_m': 6.607417, 'e_o_k': [1.101236, 0.880989], 'p_i': 20, 'u_i': 4.7114},
        {'id': 2, 'e_m': 17.470334, 'e_o_k': [1.559109, 1.247287, 0.997830, 0.798264, 0.638611], 'p_i': 40, 'u_i': 3.0006},
        {'id': 3, 'e_m': 25.015423, 'e_o_k': [3.075667, 2.460533, 1.968427], 'p_i': 80, 'u_i': 1.2816},
        {'id': 4, 'e_m': 3.215487, 'e_o_k': [0.326777, 0.261422, 0.209137, 0.167310], 'p_i': 40, 'u_i': 2.2759},
        {'id': 5, 'e_m': 9.569649, 'e_o_k': [0.778172, 0.622538, 0.498030, 0.398424, 0.318739, 0.254991], 'p_i': 20, 'u_i': 1.7983},
        {'id': 6, 'e_m': 0.145867, 'e_o_k': [0.024311, 0.019449], 'p_i': 10, 'u_i': 2.1310},
        {'id': 7, 'e_m': 6.141769, 'e_o_k': [0.499428, 0.399543, 0.319634, 0.255707, 0.204566, 0.163653], 'p_i': 20, 'u_i': 2.4443},
    ]
    B_BUDGET = 263.119998
    return processors, tasks, B_BUDGET
