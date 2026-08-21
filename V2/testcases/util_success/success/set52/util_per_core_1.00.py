"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200006, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200006, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.052962, 'e_o_k': [0.252413, 0.201931, 0.161545], 'p_i': 10, 'u_i': 4.1932},
        {'id': 1, 'e_m': 2.794123, 'e_o_k': [0.465687, 0.372550], 'p_i': 20, 'u_i': 2.7154},
        {'id': 2, 'e_m': 1.584906, 'e_o_k': [0.194865, 0.155892, 0.124714], 'p_i': 40, 'u_i': 4.3253},
        {'id': 3, 'e_m': 34.040017, 'e_o_k': [3.459351, 2.767481, 2.213985, 1.771188], 'p_i': 80, 'u_i': 1.0005},
        {'id': 4, 'e_m': 8.133570, 'e_o_k': [0.725866, 0.580693, 0.464554, 0.371643, 0.297315], 'p_i': 80, 'u_i': 1.9051},
        {'id': 5, 'e_m': 6.103811, 'e_o_k': [0.544724, 0.435779, 0.348623, 0.278899, 0.223119], 'p_i': 20, 'u_i': 2.2450},
        {'id': 6, 'e_m': 17.621942, 'e_o_k': [2.936990, 2.349592], 'p_i': 40, 'u_i': 3.5907},
        {'id': 7, 'e_m': 13.698643, 'e_o_k': [1.684259, 1.347408, 1.077926], 'p_i': 40, 'u_i': 4.3441},
    ]
    B_BUDGET = 239.200006
    return processors, tasks, B_BUDGET
