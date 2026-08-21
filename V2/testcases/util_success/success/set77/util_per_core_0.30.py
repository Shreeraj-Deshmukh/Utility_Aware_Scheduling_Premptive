"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760009, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760009, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.329540, 'e_o_k': [0.026797, 0.021438, 0.017150, 0.013720, 0.010976, 0.008781], 'p_i': 10, 'u_i': 3.3901},
        {'id': 1, 'e_m': 2.535916, 'e_o_k': [0.206212, 0.164970, 0.131976, 0.105581, 0.084465, 0.067572], 'p_i': 20, 'u_i': 2.3217},
        {'id': 2, 'e_m': 3.375830, 'e_o_k': [0.343072, 0.274458, 0.219566, 0.175653], 'p_i': 40, 'u_i': 2.1118},
        {'id': 3, 'e_m': 0.972504, 'e_o_k': [0.098832, 0.079065, 0.063252, 0.050602], 'p_i': 80, 'u_i': 4.2305},
        {'id': 4, 'e_m': 10.903455, 'e_o_k': [1.817243, 1.453794], 'p_i': 80, 'u_i': 2.0791},
        {'id': 5, 'e_m': 5.961162, 'e_o_k': [0.993527, 0.794822], 'p_i': 80, 'u_i': 1.4810},
        {'id': 6, 'e_m': 5.427089, 'e_o_k': [0.904515, 0.723612], 'p_i': 80, 'u_i': 3.5439},
        {'id': 7, 'e_m': 0.650518, 'e_o_k': [0.052898, 0.042318, 0.033855, 0.027084, 0.021667, 0.017334], 'p_i': 10, 'u_i': 4.1958},
    ]
    B_BUDGET = 71.760009
    return processors, tasks, B_BUDGET
