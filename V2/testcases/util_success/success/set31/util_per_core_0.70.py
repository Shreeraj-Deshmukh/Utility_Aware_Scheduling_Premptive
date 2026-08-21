"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440005, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440005, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.165388, 'e_o_k': [0.014760, 0.011808, 0.009446, 0.007557, 0.006046], 'p_i': 10, 'u_i': 1.6627},
        {'id': 1, 'e_m': 6.774891, 'e_o_k': [1.129149, 0.903319], 'p_i': 20, 'u_i': 3.5149},
        {'id': 2, 'e_m': 0.438988, 'e_o_k': [0.039177, 0.031341, 0.025073, 0.020058, 0.016047], 'p_i': 40, 'u_i': 4.5839},
        {'id': 3, 'e_m': 28.637798, 'e_o_k': [2.328731, 1.862985, 1.490388, 1.192310, 0.953848, 0.763078], 'p_i': 80, 'u_i': 2.6459},
        {'id': 4, 'e_m': 2.266283, 'e_o_k': [0.230313, 0.184251, 0.147400, 0.117920], 'p_i': 20, 'u_i': 4.0652},
        {'id': 5, 'e_m': 0.924968, 'e_o_k': [0.094001, 0.075201, 0.060161, 0.048128], 'p_i': 10, 'u_i': 1.7567},
        {'id': 6, 'e_m': 18.189182, 'e_o_k': [1.479084, 1.183267, 0.946614, 0.757291, 0.605833, 0.484666], 'p_i': 40, 'u_i': 2.4418},
        {'id': 7, 'e_m': 0.152289, 'e_o_k': [0.015477, 0.012381, 0.009905, 0.007924], 'p_i': 10, 'u_i': 4.3648},
    ]
    B_BUDGET = 167.440005
    return processors, tasks, B_BUDGET
