"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200014, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200014, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.521509, 'e_o_k': [0.144864, 0.115891], 'p_i': 10, 'u_i': 2.9022},
        {'id': 1, 'e_m': 1.568163, 'e_o_k': [0.233246, 0.186597, 0.149278, 0.119422, 0.095538], 'p_i': 20, 'u_i': 3.0103},
        {'id': 2, 'e_m': 1.108635, 'e_o_k': [0.187777, 0.150222, 0.120177, 0.096142], 'p_i': 40, 'u_i': 4.4931},
        {'id': 3, 'e_m': 6.413023, 'e_o_k': [0.869143, 0.695314, 0.556251, 0.445001, 0.356001, 0.284801], 'p_i': 80, 'u_i': 4.6084},
        {'id': 4, 'e_m': 0.883165, 'e_o_k': [0.245324, 0.196259], 'p_i': 10, 'u_i': 3.5739},
        {'id': 5, 'e_m': 2.929834, 'e_o_k': [0.397074, 0.317659, 0.254127, 0.203302, 0.162641, 0.130113], 'p_i': 40, 'u_i': 3.1864},
    ]
    B_BUDGET = 55.200014
    return processors, tasks, B_BUDGET
