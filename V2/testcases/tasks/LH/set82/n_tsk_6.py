"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.130582, 'e_o_k': [0.879342, 0.703474], 'p_i': 10, 'u_i': 4.0095},
        {'id': 1, 'e_m': 0.240545, 'e_o_k': [0.100180, 0.080144, 0.064115, 0.051292, 0.041034], 'p_i': 20, 'u_i': 4.5444},
        {'id': 2, 'e_m': 2.057526, 'e_o_k': [1.600298, 1.280239], 'p_i': 40, 'u_i': 4.8070},
        {'id': 3, 'e_m': 2.770051, 'e_o_k': [1.153639, 0.922911, 0.738329, 0.590663, 0.472530], 'p_i': 80, 'u_i': 3.8434},
        {'id': 4, 'e_m': 5.452928, 'e_o_k': [4.241166, 3.392933], 'p_i': 40, 'u_i': 3.7460},
        {'id': 5, 'e_m': 0.525275, 'e_o_k': [0.249114, 0.199291, 0.159433, 0.127546], 'p_i': 10, 'u_i': 2.3844},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
