"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520001, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520001, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.585755, 'e_o_k': [0.141518, 0.113214, 0.090571, 0.072457, 0.057966], 'p_i': 10, 'u_i': 1.8232},
        {'id': 1, 'e_m': 2.517453, 'e_o_k': [0.224666, 0.179732, 0.143786, 0.115029, 0.092023], 'p_i': 20, 'u_i': 4.2323},
        {'id': 2, 'e_m': 8.006401, 'e_o_k': [0.714517, 0.571614, 0.457291, 0.365833, 0.292666], 'p_i': 40, 'u_i': 3.7021},
        {'id': 3, 'e_m': 6.698806, 'e_o_k': [0.823624, 0.658899, 0.527119], 'p_i': 80, 'u_i': 1.4717},
        {'id': 4, 'e_m': 1.790065, 'e_o_k': [0.220090, 0.176072, 0.140858], 'p_i': 10, 'u_i': 2.9634},
        {'id': 5, 'e_m': 7.499195, 'e_o_k': [0.669252, 0.535402, 0.428321, 0.342657, 0.274126], 'p_i': 80, 'u_i': 1.6416},
        {'id': 6, 'e_m': 3.011229, 'e_o_k': [0.268732, 0.214985, 0.171988, 0.137591, 0.110073], 'p_i': 20, 'u_i': 4.1520},
        {'id': 7, 'e_m': 2.083489, 'e_o_k': [0.211737, 0.169389, 0.135511, 0.108409], 'p_i': 10, 'u_i': 2.8128},
    ]
    B_BUDGET = 143.520001
    return processors, tasks, B_BUDGET
