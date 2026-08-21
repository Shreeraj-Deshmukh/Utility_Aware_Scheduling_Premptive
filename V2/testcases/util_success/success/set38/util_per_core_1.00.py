"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199989, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199989, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.470709, 'e_o_k': [0.398980, 0.319184, 0.255347, 0.204278, 0.163422], 'p_i': 10, 'u_i': 2.2213},
        {'id': 1, 'e_m': 3.991035, 'e_o_k': [0.405593, 0.324474, 0.259579, 0.207664], 'p_i': 20, 'u_i': 1.5658},
        {'id': 2, 'e_m': 15.873039, 'e_o_k': [1.613114, 1.290491, 1.032393, 0.825914], 'p_i': 40, 'u_i': 3.4291},
        {'id': 3, 'e_m': 24.079760, 'e_o_k': [4.013293, 3.210635], 'p_i': 80, 'u_i': 2.0089},
        {'id': 4, 'e_m': 0.361429, 'e_o_k': [0.029390, 0.023512, 0.018810, 0.015048, 0.012038, 0.009631], 'p_i': 10, 'u_i': 2.8690},
        {'id': 5, 'e_m': 2.036313, 'e_o_k': [0.339385, 0.271508], 'p_i': 10, 'u_i': 4.7846},
        {'id': 6, 'e_m': 1.018826, 'e_o_k': [0.125266, 0.100212, 0.080170], 'p_i': 10, 'u_i': 2.6284},
        {'id': 7, 'e_m': 12.555906, 'e_o_k': [1.543759, 1.235007, 0.988006], 'p_i': 40, 'u_i': 3.5588},
    ]
    B_BUDGET = 239.199989
    return processors, tasks, B_BUDGET
