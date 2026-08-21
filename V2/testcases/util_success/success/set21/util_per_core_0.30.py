"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759984, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759984, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.518582, 'e_o_k': [0.063760, 0.051008, 0.040806], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 2.738383, 'e_o_k': [0.222676, 0.178141, 0.142513, 0.114010, 0.091208, 0.072967], 'p_i': 20, 'u_i': 1.0830},
        {'id': 2, 'e_m': 4.027282, 'e_o_k': [0.671214, 0.536971], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 7.240276, 'e_o_k': [0.588755, 0.471004, 0.376803, 0.301443, 0.241154, 0.192923], 'p_i': 80, 'u_i': 2.8864},
        {'id': 4, 'e_m': 0.567609, 'e_o_k': [0.050655, 0.040524, 0.032419, 0.025936, 0.020748], 'p_i': 10, 'u_i': 1.3892},
        {'id': 5, 'e_m': 0.562230, 'e_o_k': [0.057137, 0.045710, 0.036568, 0.029254], 'p_i': 10, 'u_i': 2.4866},
        {'id': 6, 'e_m': 5.061470, 'e_o_k': [0.451702, 0.361361, 0.289089, 0.231271, 0.185017], 'p_i': 80, 'u_i': 4.5153},
        {'id': 7, 'e_m': 1.751394, 'e_o_k': [0.156300, 0.125040, 0.100032, 0.080026, 0.064020], 'p_i': 40, 'u_i': 1.1207},
    ]
    B_BUDGET = 71.759984
    return processors, tasks, B_BUDGET
