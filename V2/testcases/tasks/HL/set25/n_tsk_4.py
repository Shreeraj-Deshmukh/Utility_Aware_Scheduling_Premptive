"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400015, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400015, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.246043, 'e_o_k': [0.665173, 0.532138, 0.425711], 'p_i': 10, 'u_i': 3.5371},
        {'id': 1, 'e_m': 7.505965, 'e_o_k': [1.538108, 1.230486, 0.984389], 'p_i': 20, 'u_i': 2.5364},
        {'id': 2, 'e_m': 2.623764, 'e_o_k': [0.444404, 0.355524, 0.284419, 0.227535], 'p_i': 40, 'u_i': 2.9162},
        {'id': 3, 'e_m': 2.760272, 'e_o_k': [0.467526, 0.374021, 0.299217, 0.239373], 'p_i': 80, 'u_i': 1.5428},
    ]
    B_BUDGET = 110.400015
    return processors, tasks, B_BUDGET
