"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.271924, 'e_o_k': [0.211496, 0.169197], 'p_i': 10, 'u_i': 4.4654},
        {'id': 1, 'e_m': 2.850575, 'e_o_k': [1.635576, 1.308461, 1.046769], 'p_i': 20, 'u_i': 1.2910},
        {'id': 2, 'e_m': 7.504114, 'e_o_k': [2.847645, 2.278116, 1.822493, 1.457994, 1.166395, 0.933116], 'p_i': 40, 'u_i': 1.4207},
        {'id': 3, 'e_m': 3.414082, 'e_o_k': [1.421857, 1.137486, 0.909989, 0.727991, 0.582393], 'p_i': 80, 'u_i': 4.1417},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
