"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280001, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280001, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.563599, 'e_o_k': [0.362154, 0.289723, 0.231779, 0.185423], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 6.547922, 'e_o_k': [1.091320, 0.873056], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 15.352271, 'e_o_k': [1.248396, 0.998717, 0.798973, 0.639179, 0.511343, 0.409074], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 6.794259, 'e_o_k': [0.835360, 0.668288, 0.534630], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 8.811924, 'e_o_k': [0.716556, 0.573245, 0.458596, 0.366877, 0.293502, 0.234801], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 6.089548, 'e_o_k': [0.748715, 0.598972, 0.479178], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 18.520414, 'e_o_k': [1.652821, 1.322257, 1.057806, 0.846245, 0.676996], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 3.072322, 'e_o_k': [0.312228, 0.249782, 0.199826, 0.159861], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 215.280001
    return processors, tasks, B_BUDGET
