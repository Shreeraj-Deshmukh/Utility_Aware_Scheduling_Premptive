"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.68, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.68, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.435325, 'e_o_k': [0.072554, 0.058043], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 3.692417, 'e_o_k': [0.375246, 0.300196, 0.240157, 0.192126], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 1.661795, 'e_o_k': [0.135132, 0.108105, 0.086484, 0.069187, 0.055350, 0.044280], 'p_i': 40, 'u_i': 3.0715},
        {'id': 3, 'e_m': 21.880045, 'e_o_k': [1.779213, 1.423370, 1.138696, 0.910957, 0.728765, 0.583012], 'p_i': 80, 'u_i': 2.1053},
        {'id': 4, 'e_m': 0.175787, 'e_o_k': [0.029298, 0.023438], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.532000, 'e_o_k': [0.088667, 0.070933], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.171451, 'e_o_k': [0.015301, 0.012241, 0.009793, 0.007834, 0.006267], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 4.085336, 'e_o_k': [0.502295, 0.401836, 0.321469], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 95.680000
    return processors, tasks, B_BUDGET
