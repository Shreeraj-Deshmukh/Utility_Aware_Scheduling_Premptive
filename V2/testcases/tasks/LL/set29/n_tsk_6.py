"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.383152, 'e_o_k': [0.056990, 0.045592, 0.036473, 0.029179, 0.023343], 'p_i': 10, 'u_i': 2.3860},
        {'id': 1, 'e_m': 0.611528, 'e_o_k': [0.169869, 0.135895], 'p_i': 20, 'u_i': 2.0962},
        {'id': 2, 'e_m': 2.560593, 'e_o_k': [0.433705, 0.346964, 0.277571, 0.222057], 'p_i': 40, 'u_i': 2.6459},
        {'id': 3, 'e_m': 2.908495, 'e_o_k': [0.394182, 0.315346, 0.252276, 0.201821, 0.161457, 0.129166], 'p_i': 80, 'u_i': 2.9249},
        {'id': 4, 'e_m': 8.125111, 'e_o_k': [1.101178, 0.880943, 0.704754, 0.563803, 0.451043, 0.360834], 'p_i': 80, 'u_i': 2.8041},
        {'id': 5, 'e_m': 5.166939, 'e_o_k': [1.435261, 1.148209], 'p_i': 40, 'u_i': 4.5045},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
