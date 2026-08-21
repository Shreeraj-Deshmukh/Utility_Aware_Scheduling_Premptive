"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360002, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360002, "H": 80, "J": 22, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.585254, 'e_o_k': [0.563761, 0.451009, 0.360807], 'p_i': 10, 'u_i': 2.1649},
        {'id': 1, 'e_m': 7.189071, 'e_o_k': [0.730597, 0.584477, 0.467582, 0.374065], 'p_i': 20, 'u_i': 4.2967},
        {'id': 2, 'e_m': 2.528917, 'e_o_k': [0.225689, 0.180551, 0.144441, 0.115553, 0.092442], 'p_i': 40, 'u_i': 4.7478},
        {'id': 3, 'e_m': 31.819722, 'e_o_k': [2.839694, 2.271756, 1.817404, 1.453924, 1.163139], 'p_i': 80, 'u_i': 1.3363},
        {'id': 4, 'e_m': 4.752739, 'e_o_k': [0.424150, 0.339320, 0.271456, 0.217165, 0.173732], 'p_i': 80, 'u_i': 1.3930},
        {'id': 5, 'e_m': 1.011392, 'e_o_k': [0.082243, 0.065794, 0.052636, 0.042108, 0.033687, 0.026949], 'p_i': 20, 'u_i': 4.7534},
        {'id': 6, 'e_m': 11.484173, 'e_o_k': [0.933855, 0.747084, 0.597667, 0.478134, 0.382507, 0.306006], 'p_i': 80, 'u_i': 2.0949},
        {'id': 7, 'e_m': 5.401644, 'e_o_k': [0.900274, 0.720219], 'p_i': 80, 'u_i': 3.1382},
    ]
    B_BUDGET = 191.360002
    return processors, tasks, B_BUDGET
