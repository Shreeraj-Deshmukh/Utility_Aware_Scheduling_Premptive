"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.416382, 'e_o_k': [0.042315, 0.033852, 0.027082, 0.021665], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 0.638595, 'e_o_k': [0.056990, 0.045592, 0.036474, 0.029179, 0.023343], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 2.546777, 'e_o_k': [0.227283, 0.181826, 0.145461, 0.116369, 0.093095], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 2.611735, 'e_o_k': [0.233080, 0.186464, 0.149171, 0.119337, 0.095469], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 3.025037, 'e_o_k': [0.504173, 0.403338], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 2.092010, 'e_o_k': [0.257214, 0.205771, 0.164617], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 2.675457, 'e_o_k': [0.271896, 0.217517, 0.174013, 0.139211], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 2.614535, 'e_o_k': [0.435756, 0.348605], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 71.760002
    return processors, tasks, B_BUDGET
