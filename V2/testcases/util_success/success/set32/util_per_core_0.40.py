"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680017, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680017, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.015283, 'e_o_k': [0.090607, 0.072486, 0.057989, 0.046391, 0.037113], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 1.338137, 'e_o_k': [0.108813, 0.087050, 0.069640, 0.055712, 0.044570, 0.035656], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 1.215369, 'e_o_k': [0.098830, 0.079064, 0.063251, 0.050601, 0.040481, 0.032385], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 11.427473, 'e_o_k': [1.904579, 1.523663], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 4.192750, 'e_o_k': [0.426093, 0.340874, 0.272699, 0.218159], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.541048, 'e_o_k': [0.054985, 0.043988, 0.035190, 0.028152], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 5.660701, 'e_o_k': [0.943450, 0.754760], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.655144, 'e_o_k': [0.109191, 0.087353], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 95.680017
    return processors, tasks, B_BUDGET
