"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280009, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280009, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.391328, 'e_o_k': [0.113138, 0.090511, 0.072408, 0.057927, 0.046341, 0.037073], 'p_i': 10, 'u_i': 1.3112},
        {'id': 1, 'e_m': 2.899140, 'e_o_k': [0.235748, 0.188599, 0.150879, 0.120703, 0.096563, 0.077250], 'p_i': 20, 'u_i': 2.1246},
        {'id': 2, 'e_m': 2.752107, 'e_o_k': [0.223792, 0.179034, 0.143227, 0.114582, 0.091665, 0.073332], 'p_i': 40, 'u_i': 2.2214},
        {'id': 3, 'e_m': 11.407432, 'e_o_k': [1.018036, 0.814429, 0.651543, 0.521234, 0.416988], 'p_i': 80, 'u_i': 3.1164},
        {'id': 4, 'e_m': 3.738741, 'e_o_k': [0.333657, 0.266926, 0.213541, 0.170833, 0.136666], 'p_i': 10, 'u_i': 2.9383},
        {'id': 5, 'e_m': 35.429522, 'e_o_k': [3.161845, 2.529476, 2.023581, 1.618864, 1.295092], 'p_i': 80, 'u_i': 2.8468},
        {'id': 6, 'e_m': 2.532635, 'e_o_k': [0.422106, 0.337685], 'p_i': 10, 'u_i': 4.6487},
        {'id': 7, 'e_m': 2.345080, 'e_o_k': [0.390847, 0.312677], 'p_i': 10, 'u_i': 3.0837},
    ]
    B_BUDGET = 215.280009
    return processors, tasks, B_BUDGET
