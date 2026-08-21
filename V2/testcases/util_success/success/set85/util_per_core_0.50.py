"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599999, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599999, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.610550, 'e_o_k': [0.101758, 0.081407], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 1.155819, 'e_o_k': [0.117461, 0.093969, 0.075175, 0.060140], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 2.860408, 'e_o_k': [0.255272, 0.204218, 0.163374, 0.130699, 0.104559], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 5.821513, 'e_o_k': [0.715760, 0.572608, 0.458086], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.180959, 'e_o_k': [0.014715, 0.011772, 0.009418, 0.007534, 0.006027, 0.004822], 'p_i': 10, 'u_i': 1.9890},
        {'id': 5, 'e_m': 0.176193, 'e_o_k': [0.021663, 0.017330, 0.013864], 'p_i': 40, 'u_i': 1.7667},
        {'id': 6, 'e_m': 6.155841, 'e_o_k': [0.756866, 0.605493, 0.484394], 'p_i': 20, 'u_i': 2.7743},
        {'id': 7, 'e_m': 4.065821, 'e_o_k': [0.413193, 0.330555, 0.264444, 0.211555], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 119.599999
    return processors, tasks, B_BUDGET
