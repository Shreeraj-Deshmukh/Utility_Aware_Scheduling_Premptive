"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.505129, 'e_o_k': [0.152960, 0.122368, 0.097895, 0.078316], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.107895, 'e_o_k': [0.010965, 0.008772, 0.007018, 0.005614], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 3.273963, 'e_o_k': [0.292179, 0.233743, 0.186995, 0.149596, 0.119677], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 1.440861, 'e_o_k': [0.177155, 0.141724, 0.113379], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 2.527032, 'e_o_k': [0.225520, 0.180416, 0.144333, 0.115466, 0.092373], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 1.051815, 'e_o_k': [0.129322, 0.103457, 0.082766], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 5.112845, 'e_o_k': [0.628628, 0.502903, 0.402322], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 1.645554, 'e_o_k': [0.167231, 0.133785, 0.107028, 0.085622], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 71.760003
    return processors, tasks, B_BUDGET
