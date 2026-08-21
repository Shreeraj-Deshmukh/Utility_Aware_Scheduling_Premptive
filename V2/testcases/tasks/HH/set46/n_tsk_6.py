"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.147430, 'e_o_k': [0.892445, 0.713956], 'p_i': 10, 'u_i': 2.0200},
        {'id': 1, 'e_m': 0.711598, 'e_o_k': [0.408294, 0.326635, 0.261308], 'p_i': 20, 'u_i': 3.9687},
        {'id': 2, 'e_m': 14.390903, 'e_o_k': [5.461029, 4.368823, 3.495059, 2.796047, 2.236837, 1.789470], 'p_i': 40, 'u_i': 2.3030},
        {'id': 3, 'e_m': 9.199953, 'e_o_k': [5.278662, 4.222929, 3.378344], 'p_i': 80, 'u_i': 2.6501},
        {'id': 4, 'e_m': 1.420179, 'e_o_k': [0.591460, 0.473168, 0.378534, 0.302827, 0.242262], 'p_i': 10, 'u_i': 1.7748},
        {'id': 5, 'e_m': 0.657744, 'e_o_k': [0.377394, 0.301915, 0.241532], 'p_i': 20, 'u_i': 3.9815},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
