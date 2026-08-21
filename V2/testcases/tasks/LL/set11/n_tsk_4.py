"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.136367, 'e_o_k': [0.169022, 0.135217, 0.108174, 0.086539, 0.069231], 'p_i': 10, 'u_i': 2.5944},
        {'id': 1, 'e_m': 4.722654, 'e_o_k': [0.702441, 0.561953, 0.449563, 0.359650, 0.287720], 'p_i': 20, 'u_i': 4.8069},
        {'id': 2, 'e_m': 1.652632, 'e_o_k': [0.279917, 0.223934, 0.179147, 0.143318], 'p_i': 40, 'u_i': 1.7136},
        {'id': 3, 'e_m': 0.713186, 'e_o_k': [0.106078, 0.084863, 0.067890, 0.054312, 0.043450], 'p_i': 80, 'u_i': 3.6562},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
