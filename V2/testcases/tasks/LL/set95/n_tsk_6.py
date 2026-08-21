"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.062885, 'e_o_k': [0.180028, 0.144022, 0.115218, 0.092174], 'p_i': 10, 'u_i': 2.8802},
        {'id': 1, 'e_m': 1.880293, 'e_o_k': [0.318478, 0.254782, 0.203826, 0.163061], 'p_i': 20, 'u_i': 1.9313},
        {'id': 2, 'e_m': 4.030110, 'e_o_k': [1.119475, 0.895580], 'p_i': 40, 'u_i': 4.0147},
        {'id': 3, 'e_m': 1.729233, 'e_o_k': [0.234359, 0.187487, 0.149990, 0.119992, 0.095994, 0.076795], 'p_i': 80, 'u_i': 3.8759},
        {'id': 4, 'e_m': 2.650485, 'e_o_k': [0.543132, 0.434506, 0.347605], 'p_i': 80, 'u_i': 4.3076},
        {'id': 5, 'e_m': 3.535813, 'e_o_k': [0.479201, 0.383361, 0.306689, 0.245351, 0.196281, 0.157025], 'p_i': 80, 'u_i': 1.9116},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
