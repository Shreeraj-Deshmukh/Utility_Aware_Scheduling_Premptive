"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.261165, 'e_o_k': [1.758684, 1.406947], 'p_i': 10, 'u_i': 4.0095},
        {'id': 1, 'e_m': 0.481091, 'e_o_k': [0.200359, 0.160287, 0.128230, 0.102584, 0.082067], 'p_i': 20, 'u_i': 4.5444},
        {'id': 2, 'e_m': 4.115053, 'e_o_k': [3.200597, 2.560477], 'p_i': 40, 'u_i': 4.8070},
        {'id': 3, 'e_m': 5.540102, 'e_o_k': [2.307277, 1.845822, 1.476657, 1.181326, 0.945061], 'p_i': 80, 'u_i': 3.8434},
        {'id': 4, 'e_m': 10.905856, 'e_o_k': [8.482333, 6.785866], 'p_i': 40, 'u_i': 3.7460},
        {'id': 5, 'e_m': 1.050550, 'e_o_k': [0.498228, 0.398583, 0.318866, 0.255093], 'p_i': 10, 'u_i': 2.3844},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET
