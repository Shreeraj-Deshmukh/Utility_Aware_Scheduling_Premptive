"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.27998, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.27998, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.576724, 'e_o_k': [0.261862, 0.209490, 0.167592, 0.134073], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 2.544986, 'e_o_k': [0.206950, 0.165560, 0.132448, 0.105958, 0.084767, 0.067813], 'p_i': 20, 'u_i': 1.5082},
        {'id': 2, 'e_m': 3.680458, 'e_o_k': [0.374030, 0.299224, 0.239379, 0.191504], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 23.061688, 'e_o_k': [2.343667, 1.874934, 1.499947, 1.199958], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 9.526301, 'e_o_k': [0.774647, 0.619718, 0.495774, 0.396619, 0.317295, 0.253836], 'p_i': 20, 'u_i': 2.1026},
        {'id': 5, 'e_m': 0.984294, 'e_o_k': [0.080040, 0.064032, 0.051225, 0.040980, 0.032784, 0.026227], 'p_i': 10, 'u_i': 4.2691},
        {'id': 6, 'e_m': 4.711364, 'e_o_k': [0.383112, 0.306490, 0.245192, 0.196154, 0.156923, 0.125538], 'p_i': 20, 'u_i': 3.6679},
        {'id': 7, 'e_m': 17.958642, 'e_o_k': [2.993107, 2.394486], 'p_i': 80, 'u_i': 2.7165},
    ]
    B_BUDGET = 215.279980
    return processors, tasks, B_BUDGET
