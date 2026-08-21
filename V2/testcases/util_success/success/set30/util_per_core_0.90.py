"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.28001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.28001, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.730195, 'e_o_k': [0.455032, 0.364026], 'p_i': 10, 'u_i': 3.4672},
        {'id': 1, 'e_m': 3.903458, 'e_o_k': [0.348357, 0.278686, 0.222949, 0.178359, 0.142687], 'p_i': 20, 'u_i': 1.7093},
        {'id': 2, 'e_m': 9.912434, 'e_o_k': [1.007361, 0.805889, 0.644711, 0.515769], 'p_i': 40, 'u_i': 4.7778},
        {'id': 3, 'e_m': 32.180248, 'e_o_k': [2.871869, 2.297495, 1.837996, 1.470397, 1.176317], 'p_i': 80, 'u_i': 2.0901},
        {'id': 4, 'e_m': 1.072290, 'e_o_k': [0.095695, 0.076556, 0.061245, 0.048996, 0.039197], 'p_i': 20, 'u_i': 2.4114},
        {'id': 5, 'e_m': 0.407606, 'e_o_k': [0.033145, 0.026516, 0.021213, 0.016970, 0.013576, 0.010861], 'p_i': 80, 'u_i': 4.9042},
        {'id': 6, 'e_m': 3.061831, 'e_o_k': [0.273248, 0.218598, 0.174879, 0.139903, 0.111922], 'p_i': 20, 'u_i': 1.5854},
        {'id': 7, 'e_m': 18.797701, 'e_o_k': [1.528567, 1.222853, 0.978283, 0.782626, 0.626101, 0.500881], 'p_i': 40, 'u_i': 1.1920},
    ]
    B_BUDGET = 215.280010
    return processors, tasks, B_BUDGET
