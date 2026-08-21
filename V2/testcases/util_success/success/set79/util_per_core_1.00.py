"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199995, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199995, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.433569, 'e_o_k': [0.035256, 0.028205, 0.022564, 0.018051, 0.014441, 0.011553], 'p_i': 10, 'u_i': 3.1766},
        {'id': 1, 'e_m': 8.153191, 'e_o_k': [0.662990, 0.530392, 0.424314, 0.339451, 0.271561, 0.217249], 'p_i': 20, 'u_i': 1.6887},
        {'id': 2, 'e_m': 2.292164, 'e_o_k': [0.204560, 0.163648, 0.130918, 0.104735, 0.083788], 'p_i': 40, 'u_i': 3.5480},
        {'id': 3, 'e_m': 29.441997, 'e_o_k': [2.992073, 2.393658, 1.914927, 1.531941], 'p_i': 80, 'u_i': 3.7765},
        {'id': 4, 'e_m': 13.331187, 'e_o_k': [1.189718, 0.951774, 0.761420, 0.609136, 0.487308], 'p_i': 40, 'u_i': 3.9794},
        {'id': 5, 'e_m': 13.973748, 'e_o_k': [1.718084, 1.374467, 1.099574], 'p_i': 80, 'u_i': 3.8371},
        {'id': 6, 'e_m': 3.750877, 'e_o_k': [0.625146, 0.500117], 'p_i': 10, 'u_i': 4.0284},
        {'id': 7, 'e_m': 19.249224, 'e_o_k': [1.565283, 1.252226, 1.001781, 0.801425, 0.641140, 0.512912], 'p_i': 80, 'u_i': 4.5608},
    ]
    B_BUDGET = 239.199995
    return processors, tasks, B_BUDGET
