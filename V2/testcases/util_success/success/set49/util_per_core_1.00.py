"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199977, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199977, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.307856, 'e_o_k': [0.106350, 0.085080, 0.068064, 0.054451, 0.043561, 0.034849], 'p_i': 10, 'u_i': 4.3861},
        {'id': 1, 'e_m': 0.715248, 'e_o_k': [0.063831, 0.051065, 0.040852, 0.032681, 0.026145], 'p_i': 20, 'u_i': 4.5789},
        {'id': 2, 'e_m': 17.063419, 'e_o_k': [2.843903, 2.275123], 'p_i': 40, 'u_i': 1.9644},
        {'id': 3, 'e_m': 16.646272, 'e_o_k': [1.485567, 1.188454, 0.950763, 0.760610, 0.608488], 'p_i': 80, 'u_i': 2.9794},
        {'id': 4, 'e_m': 18.492079, 'e_o_k': [1.879276, 1.503421, 1.202737, 0.962189], 'p_i': 40, 'u_i': 1.4586},
        {'id': 5, 'e_m': 3.022307, 'e_o_k': [0.245764, 0.196611, 0.157289, 0.125831, 0.100665, 0.080532], 'p_i': 10, 'u_i': 1.4184},
        {'id': 6, 'e_m': 3.139644, 'e_o_k': [0.386022, 0.308817, 0.247054], 'p_i': 10, 'u_i': 1.6447},
        {'id': 7, 'e_m': 2.405822, 'e_o_k': [0.195633, 0.156507, 0.125205, 0.100164, 0.080131, 0.064105], 'p_i': 20, 'u_i': 4.2787},
    ]
    B_BUDGET = 239.199977
    return processors, tasks, B_BUDGET
