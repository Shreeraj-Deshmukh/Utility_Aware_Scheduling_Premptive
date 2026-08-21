"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.263700, 'e_o_k': [0.035739, 0.028591, 0.022873, 0.018298, 0.014639, 0.011711], 'p_i': 10, 'u_i': 3.5665},
        {'id': 1, 'e_m': 2.217666, 'e_o_k': [0.375621, 0.300497, 0.240397, 0.192318], 'p_i': 20, 'u_i': 1.8299},
        {'id': 2, 'e_m': 6.413922, 'e_o_k': [1.781645, 1.425316], 'p_i': 40, 'u_i': 2.7998},
        {'id': 3, 'e_m': 8.191891, 'e_o_k': [2.275525, 1.820420], 'p_i': 80, 'u_i': 4.4830},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
