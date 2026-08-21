"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200008, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200008, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.851681, 'e_o_k': [0.808613, 0.646891], 'p_i': 10, 'u_i': 1.7372},
        {'id': 1, 'e_m': 3.069102, 'e_o_k': [0.511517, 0.409214], 'p_i': 20, 'u_i': 2.9397},
        {'id': 2, 'e_m': 2.793354, 'e_o_k': [0.283877, 0.227102, 0.181682, 0.145345], 'p_i': 40, 'u_i': 2.9966},
        {'id': 3, 'e_m': 15.516022, 'e_o_k': [1.384700, 1.107760, 0.886208, 0.708966, 0.567173], 'p_i': 80, 'u_i': 2.3520},
        {'id': 4, 'e_m': 23.933337, 'e_o_k': [2.942623, 2.354099, 1.883279], 'p_i': 80, 'u_i': 2.7023},
        {'id': 5, 'e_m': 0.007855, 'e_o_k': [0.000966, 0.000773, 0.000618], 'p_i': 10, 'u_i': 3.3163},
        {'id': 6, 'e_m': 9.522866, 'e_o_k': [0.849851, 0.679881, 0.543905, 0.435124, 0.348099], 'p_i': 20, 'u_i': 4.1370},
        {'id': 7, 'e_m': 25.719775, 'e_o_k': [2.295316, 1.836252, 1.469002, 1.175202, 0.940161], 'p_i': 80, 'u_i': 4.8327},
    ]
    B_BUDGET = 239.200008
    return processors, tasks, B_BUDGET
