"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679988, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679988, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.808019, 'e_o_k': [0.065705, 0.052564, 0.042051, 0.033641, 0.026913, 0.021530], 'p_i': 10, 'u_i': 2.7135},
        {'id': 1, 'e_m': 2.624685, 'e_o_k': [0.213431, 0.170745, 0.136596, 0.109276, 0.087421, 0.069937], 'p_i': 20, 'u_i': 1.9259},
        {'id': 2, 'e_m': 3.033921, 'e_o_k': [0.308325, 0.246660, 0.197328, 0.157863], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 20.140991, 'e_o_k': [1.797447, 1.437957, 1.150366, 0.920293, 0.736234], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 2.165693, 'e_o_k': [0.266274, 0.213019, 0.170415], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.136094, 'e_o_k': [0.013831, 0.011065, 0.008852, 0.007081], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 3.875810, 'e_o_k': [0.393883, 0.315106, 0.252085, 0.201668], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.483689, 'e_o_k': [0.049155, 0.039324, 0.031459, 0.025168], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 95.679988
    return processors, tasks, B_BUDGET
