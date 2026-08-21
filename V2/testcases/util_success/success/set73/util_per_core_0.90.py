"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28001, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28001, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.300778, 'e_o_k': [0.105775, 0.084620, 0.067696, 0.054157, 0.043325, 0.034660], 'p_i': 10, 'u_i': 1.8586},
        {'id': 1, 'e_m': 0.954646, 'e_o_k': [0.117375, 0.093900, 0.075120], 'p_i': 20, 'u_i': 3.5571},
        {'id': 2, 'e_m': 11.586013, 'e_o_k': [0.942136, 0.753709, 0.602967, 0.482374, 0.385899, 0.308719], 'p_i': 40, 'u_i': 3.6967},
        {'id': 3, 'e_m': 37.832378, 'e_o_k': [4.651522, 3.721218, 2.976974], 'p_i': 80, 'u_i': 3.6040},
        {'id': 4, 'e_m': 2.350011, 'e_o_k': [0.191095, 0.152876, 0.122301, 0.097841, 0.078273, 0.062618], 'p_i': 10, 'u_i': 3.9239},
        {'id': 5, 'e_m': 6.532607, 'e_o_k': [0.531210, 0.424968, 0.339974, 0.271979, 0.217584, 0.174067], 'p_i': 20, 'u_i': 1.7810},
        {'id': 6, 'e_m': 4.195727, 'e_o_k': [0.374440, 0.299552, 0.239642, 0.191713, 0.153371], 'p_i': 20, 'u_i': 3.2318},
        {'id': 7, 'e_m': 7.057365, 'e_o_k': [0.867709, 0.694167, 0.555334], 'p_i': 80, 'u_i': 1.5696},
    ]
    B_BUDGET = 215.280010
    return processors, tasks, B_BUDGET
