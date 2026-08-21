"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120007, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120007, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.867449, 'e_o_k': [0.345144, 0.276115, 0.220892, 0.176714, 0.141371], 'p_i': 10, 'u_i': 2.7373},
        {'id': 1, 'e_m': 9.316775, 'e_o_k': [0.757609, 0.606087, 0.484870, 0.387896, 0.310317, 0.248253], 'p_i': 20, 'u_i': 1.7250},
        {'id': 2, 'e_m': 13.718925, 'e_o_k': [1.115577, 0.892462, 0.713970, 0.571176, 0.456941, 0.365552], 'p_i': 40, 'u_i': 4.5633},
        {'id': 3, 'e_m': 37.234005, 'e_o_k': [6.205667, 4.964534], 'p_i': 80, 'u_i': 2.2095},
        {'id': 4, 'e_m': 5.740057, 'e_o_k': [0.466762, 0.373410, 0.298728, 0.238982, 0.191186, 0.152949], 'p_i': 40, 'u_i': 2.7670},
        {'id': 5, 'e_m': 2.604246, 'e_o_k': [0.434041, 0.347233], 'p_i': 10, 'u_i': 1.9794},
        {'id': 6, 'e_m': 1.243685, 'e_o_k': [0.207281, 0.165825], 'p_i': 40, 'u_i': 3.2273},
        {'id': 7, 'e_m': 4.159999, 'e_o_k': [0.422764, 0.338211, 0.270569, 0.216455], 'p_i': 40, 'u_i': 2.4110},
    ]
    B_BUDGET = 263.120007
    return processors, tasks, B_BUDGET
