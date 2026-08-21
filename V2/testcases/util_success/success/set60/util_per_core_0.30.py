"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760005, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760005, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.092466, 'e_o_k': [0.111023, 0.088818, 0.071055, 0.056844], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 4.854737, 'e_o_k': [0.596894, 0.477515, 0.382012], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 0.802523, 'e_o_k': [0.098671, 0.078937, 0.063149], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 7.125732, 'e_o_k': [0.579441, 0.463553, 0.370842, 0.296674, 0.237339, 0.189871], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.274077, 'e_o_k': [0.045679, 0.036544], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.138033, 'e_o_k': [0.016971, 0.013577, 0.010862], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 3.962000, 'e_o_k': [0.402642, 0.322114, 0.257691, 0.206153], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.191766, 'e_o_k': [0.019488, 0.015591, 0.012473, 0.009978], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 71.760005
    return processors, tasks, B_BUDGET
