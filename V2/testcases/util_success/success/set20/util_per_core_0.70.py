"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439978, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439978, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.750837, 'e_o_k': [0.334737, 0.267789, 0.214232, 0.171385, 0.137108], 'p_i': 10, 'u_i': 1.5090},
        {'id': 1, 'e_m': 2.474420, 'e_o_k': [0.201212, 0.160969, 0.128775, 0.103020, 0.082416, 0.065933], 'p_i': 20, 'u_i': 3.9781},
        {'id': 2, 'e_m': 5.955023, 'e_o_k': [0.732175, 0.585740, 0.468592], 'p_i': 40, 'u_i': 2.6834},
        {'id': 3, 'e_m': 21.002298, 'e_o_k': [3.500383, 2.800306], 'p_i': 80, 'u_i': 1.3712},
        {'id': 4, 'e_m': 1.554261, 'e_o_k': [0.138707, 0.110966, 0.088773, 0.071018, 0.056815], 'p_i': 40, 'u_i': 4.1249},
        {'id': 5, 'e_m': 4.050744, 'e_o_k': [0.329393, 0.263514, 0.210812, 0.168649, 0.134919, 0.107936], 'p_i': 40, 'u_i': 1.3639},
        {'id': 6, 'e_m': 17.774403, 'e_o_k': [1.586245, 1.268996, 1.015197, 0.812157, 0.649726], 'p_i': 80, 'u_i': 1.0001},
        {'id': 7, 'e_m': 1.274858, 'e_o_k': [0.113772, 0.091018, 0.072814, 0.058251, 0.046601], 'p_i': 10, 'u_i': 1.8994},
    ]
    B_BUDGET = 167.439978
    return processors, tasks, B_BUDGET
