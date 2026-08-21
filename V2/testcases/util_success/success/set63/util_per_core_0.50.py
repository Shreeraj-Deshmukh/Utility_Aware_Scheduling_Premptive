"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600001, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600001, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.059108, 'e_o_k': [0.167440, 0.133952, 0.107162, 0.085729, 0.068583, 0.054867], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.042875, 'e_o_k': [0.004357, 0.003486, 0.002789, 0.002231], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 3.657365, 'e_o_k': [0.609561, 0.487649], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 2.069052, 'e_o_k': [0.254392, 0.203513, 0.162811], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 1.222655, 'e_o_k': [0.109114, 0.087291, 0.069833, 0.055866, 0.044693], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 2.335390, 'e_o_k': [0.237336, 0.189869, 0.151895, 0.121516], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 19.291270, 'e_o_k': [1.960495, 1.568396, 1.254717, 1.003773], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 12.559589, 'e_o_k': [1.544212, 1.235369, 0.988296], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 119.600001
    return processors, tasks, B_BUDGET
