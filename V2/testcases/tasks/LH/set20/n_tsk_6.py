"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.415096, 'e_o_k': [0.589343, 0.471474, 0.377179, 0.301743, 0.241395], 'p_i': 10, 'u_i': 3.0842},
        {'id': 1, 'e_m': 0.907251, 'e_o_k': [0.430268, 0.344215, 0.275372, 0.220297], 'p_i': 20, 'u_i': 4.6180},
        {'id': 2, 'e_m': 2.215453, 'e_o_k': [0.922666, 0.738133, 0.590506, 0.472405, 0.377924], 'p_i': 40, 'u_i': 1.1953},
        {'id': 3, 'e_m': 7.270569, 'e_o_k': [4.171638, 3.337310, 2.669848], 'p_i': 80, 'u_i': 1.1811},
        {'id': 4, 'e_m': 0.587338, 'e_o_k': [0.244608, 0.195686, 0.156549, 0.125239, 0.100191], 'p_i': 40, 'u_i': 1.7367},
        {'id': 5, 'e_m': 2.087040, 'e_o_k': [0.791985, 0.633588, 0.506871, 0.405496, 0.324397, 0.259518], 'p_i': 40, 'u_i': 3.6203},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
