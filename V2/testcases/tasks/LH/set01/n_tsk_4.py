"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.291918, 'e_o_k': [0.227047, 0.181638], 'p_i': 10, 'u_i': 3.2224},
        {'id': 1, 'e_m': 5.620499, 'e_o_k': [2.340760, 1.872608, 1.498086, 1.198469, 0.958775], 'p_i': 20, 'u_i': 4.1436},
        {'id': 2, 'e_m': 0.861058, 'e_o_k': [0.358603, 0.286883, 0.229506, 0.183605, 0.146884], 'p_i': 40, 'u_i': 3.8879},
        {'id': 3, 'e_m': 5.460544, 'e_o_k': [2.072155, 1.657724, 1.326180, 1.060944, 0.848755, 0.679004], 'p_i': 80, 'u_i': 3.5961},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
