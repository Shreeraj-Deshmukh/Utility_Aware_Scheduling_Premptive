"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519997, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519997, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.466086, 'e_o_k': [0.220081, 0.176065, 0.140852, 0.112682, 0.090145], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.475819, 'e_o_k': [0.058502, 0.046802, 0.037442], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 1.754122, 'e_o_k': [0.156544, 0.125235, 0.100188, 0.080150, 0.064120], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 18.455858, 'e_o_k': [2.269163, 1.815330, 1.452264], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 3.626541, 'e_o_k': [0.368551, 0.294841, 0.235873, 0.188698], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 2.642675, 'e_o_k': [0.440446, 0.352357], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 1.555143, 'e_o_k': [0.138786, 0.111029, 0.088823, 0.071058, 0.056847], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 3.411520, 'e_o_k': [0.304455, 0.243564, 0.194851, 0.155881, 0.124705], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 143.519997
    return processors, tasks, B_BUDGET
