"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.35999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.35999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.168911, 'e_o_k': [0.361485, 0.289188], 'p_i': 10, 'u_i': 2.4344},
        {'id': 1, 'e_m': 6.671677, 'e_o_k': [0.595402, 0.476322, 0.381057, 0.304846, 0.243877], 'p_i': 20, 'u_i': 4.3497},
        {'id': 2, 'e_m': 7.381759, 'e_o_k': [1.230293, 0.984235], 'p_i': 40, 'u_i': 1.9085},
        {'id': 3, 'e_m': 27.657023, 'e_o_k': [2.248977, 1.799182, 1.439345, 1.151476, 0.921181, 0.736945], 'p_i': 80, 'u_i': 4.5985},
        {'id': 4, 'e_m': 1.472645, 'e_o_k': [0.181063, 0.144850, 0.115880], 'p_i': 10, 'u_i': 1.1568},
        {'id': 5, 'e_m': 0.241852, 'e_o_k': [0.024578, 0.019663, 0.015730, 0.012584], 'p_i': 40, 'u_i': 3.3218},
        {'id': 6, 'e_m': 14.255440, 'e_o_k': [1.159205, 0.927364, 0.741891, 0.593513, 0.474810, 0.379848], 'p_i': 40, 'u_i': 3.9399},
        {'id': 7, 'e_m': 0.382858, 'e_o_k': [0.063810, 0.051048], 'p_i': 40, 'u_i': 2.8364},
    ]
    B_BUDGET = 191.359990
    return processors, tasks, B_BUDGET
