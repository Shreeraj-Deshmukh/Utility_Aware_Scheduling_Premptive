"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.274433, 'e_o_k': [0.130151, 0.104121, 0.083297, 0.066637], 'p_i': 10, 'u_i': 2.8575},
        {'id': 1, 'e_m': 1.031563, 'e_o_k': [0.429613, 0.343691, 0.274953, 0.219962, 0.175970], 'p_i': 20, 'u_i': 2.8209},
        {'id': 2, 'e_m': 0.135038, 'e_o_k': [0.105029, 0.084023], 'p_i': 40, 'u_i': 2.9332},
        {'id': 3, 'e_m': 2.013335, 'e_o_k': [1.155192, 0.924154, 0.739323], 'p_i': 80, 'u_i': 1.0372},
        {'id': 4, 'e_m': 2.006057, 'e_o_k': [1.151016, 0.920813, 0.736650], 'p_i': 10, 'u_i': 1.7921},
        {'id': 5, 'e_m': 3.673209, 'e_o_k': [1.393901, 1.115121, 0.892097, 0.713677, 0.570942, 0.456754], 'p_i': 40, 'u_i': 1.1296},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
