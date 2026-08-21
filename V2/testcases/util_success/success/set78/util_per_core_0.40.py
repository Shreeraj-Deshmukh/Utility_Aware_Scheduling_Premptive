"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679998, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679998, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.286440, 'e_o_k': [0.232362, 0.185889, 0.148712, 0.118969], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 1.443240, 'e_o_k': [0.128799, 0.103040, 0.082432, 0.065945, 0.052756], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 1.122430, 'e_o_k': [0.187072, 0.149657], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 19.814276, 'e_o_k': [2.013646, 1.610917, 1.288733, 1.030987], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 1.849800, 'e_o_k': [0.308300, 0.246640], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 2.622764, 'e_o_k': [0.437127, 0.349702], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.305518, 'e_o_k': [0.050920, 0.040736], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 2.463653, 'e_o_k': [0.250371, 0.200297, 0.160238, 0.128190], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 95.679998
    return processors, tasks, B_BUDGET
