"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.6, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.6, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.858180, 'e_o_k': [0.105514, 0.084411, 0.067529], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 1.978424, 'e_o_k': [0.329737, 0.263790], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 6.383921, 'e_o_k': [0.648773, 0.519018, 0.415214, 0.332172], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.282237, 'e_o_k': [0.028683, 0.022946, 0.018357, 0.014685], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 12.535506, 'e_o_k': [1.118709, 0.894967, 0.715974, 0.572779, 0.458223], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 6.738547, 'e_o_k': [0.547956, 0.438365, 0.350692, 0.280554, 0.224443, 0.179554], 'p_i': 40, 'u_i': 4.5618},
        {'id': 6, 'e_m': 0.332984, 'e_o_k': [0.055497, 0.044398], 'p_i': 10, 'u_i': 3.9189},
        {'id': 7, 'e_m': 5.479404, 'e_o_k': [0.556850, 0.445480, 0.356384, 0.285107], 'p_i': 40, 'u_i': 2.1344},
    ]
    B_BUDGET = 119.600000
    return processors, tasks, B_BUDGET
