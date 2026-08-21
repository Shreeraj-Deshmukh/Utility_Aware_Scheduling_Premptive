"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 36.799995, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.0, "seed": 1099, "set": 99, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.00"}
"""

_SPEC = '{"B": 36.799995, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.0, "seed": 1099, "set": 99, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.485314, 'e_o_k': [0.072185, 0.057748, 0.046198, 0.036959, 0.029567], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 1.461505, 'e_o_k': [0.217382, 0.173906, 0.139125, 0.111300, 0.089040], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 0.554952, 'e_o_k': [0.093996, 0.075197, 0.060157, 0.048126], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 1.824306, 'e_o_k': [0.373833, 0.299067, 0.239253], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 0.517558, 'e_o_k': [0.106057, 0.084846, 0.067876], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 5.062609, 'e_o_k': [0.753006, 0.602405, 0.481924, 0.385539, 0.308431], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 2.445941, 'e_o_k': [0.501217, 0.400974, 0.320779], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.179690, 'e_o_k': [0.049914, 0.039931], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 36.799995
    return processors, tasks, B_BUDGET
