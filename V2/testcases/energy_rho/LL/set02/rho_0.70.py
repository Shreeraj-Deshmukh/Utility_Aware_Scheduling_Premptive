"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 49.68, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.7, "seed": 1002, "set": 2, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}
"""

_SPEC = '{"B": 49.68, "H": 80, "J": 32, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.7, "seed": 1002, "set": 2, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.355801, 'e_o_k': [0.098834, 0.079067], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 0.978019, 'e_o_k': [0.132549, 0.106039, 0.084831, 0.067865, 0.054292, 0.043434], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 3.289454, 'e_o_k': [0.674068, 0.539255, 0.431404], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 7.449156, 'e_o_k': [1.526466, 1.221173, 0.976938], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 2.409551, 'e_o_k': [0.408122, 0.326497, 0.261198, 0.208958], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.229718, 'e_o_k': [0.031133, 0.024907, 0.019925, 0.015940, 0.012752, 0.010202], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 0.659831, 'e_o_k': [0.098142, 0.078514, 0.062811, 0.050249, 0.040199], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 1.081708, 'e_o_k': [0.300474, 0.240380], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 49.680000
    return processors, tasks, B_BUDGET
