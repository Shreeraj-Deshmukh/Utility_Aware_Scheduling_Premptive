"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280006, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280006, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.502174, 'e_o_k': [0.152660, 0.122128, 0.097702, 0.078162], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 2.301312, 'e_o_k': [0.233873, 0.187099, 0.149679, 0.119743], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 11.143478, 'e_o_k': [1.857246, 1.485797], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 16.937102, 'e_o_k': [2.082431, 1.665944, 1.332756], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 1.183327, 'e_o_k': [0.145491, 0.116393, 0.093114], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 35.328283, 'e_o_k': [5.888047, 4.710438], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 13.958165, 'e_o_k': [2.326361, 1.861089], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 17.942038, 'e_o_k': [2.990340, 2.392272], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 215.280006
    return processors, tasks, B_BUDGET
