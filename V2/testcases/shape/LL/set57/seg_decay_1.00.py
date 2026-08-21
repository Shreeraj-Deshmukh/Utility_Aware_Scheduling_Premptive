"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199975, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.199975, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100744, 'e_o_k': [0.010074, 0.010074, 0.010074, 0.010074, 0.010074], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 0.720915, 'e_o_k': [0.060076, 0.060076, 0.060076, 0.060076, 0.060076, 0.060076], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 4.330945, 'e_o_k': [1.082736, 1.082736], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 4.451086, 'e_o_k': [1.112772, 1.112772], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 2.996813, 'e_o_k': [0.749203, 0.749203], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 2.171206, 'e_o_k': [0.180934, 0.180934, 0.180934, 0.180934, 0.180934, 0.180934], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 0.650677, 'e_o_k': [0.162669, 0.162669], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 1.827166, 'e_o_k': [0.304528, 0.304528, 0.304528], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 55.199975
    return processors, tasks, B_BUDGET
