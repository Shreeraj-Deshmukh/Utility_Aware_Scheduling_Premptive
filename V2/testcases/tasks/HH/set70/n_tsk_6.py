"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.524362, 'e_o_k': [1.185615, 0.948492], 'p_i': 10, 'u_i': 1.8882},
        {'id': 1, 'e_m': 5.856002, 'e_o_k': [2.438839, 1.951072, 1.560857, 1.248686, 0.998949], 'p_i': 20, 'u_i': 2.0463},
        {'id': 2, 'e_m': 10.767148, 'e_o_k': [4.484176, 3.587341, 2.869873, 2.295898, 1.836719], 'p_i': 40, 'u_i': 1.5718},
        {'id': 3, 'e_m': 2.833997, 'e_o_k': [2.204220, 1.763376], 'p_i': 80, 'u_i': 2.9208},
        {'id': 4, 'e_m': 0.148278, 'e_o_k': [0.056268, 0.045015, 0.036012, 0.028809, 0.023047, 0.018438], 'p_i': 20, 'u_i': 4.6964},
        {'id': 5, 'e_m': 3.419689, 'e_o_k': [1.962116, 1.569693, 1.255755], 'p_i': 80, 'u_i': 4.6519},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
