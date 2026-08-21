"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.544221, 'e_o_k': [0.423283, 0.338626], 'p_i': 10, 'u_i': 3.6581},
        {'id': 1, 'e_m': 0.741296, 'e_o_k': [0.308726, 0.246981, 0.197585, 0.158068, 0.126454], 'p_i': 20, 'u_i': 4.4037},
        {'id': 2, 'e_m': 5.236422, 'e_o_k': [1.987106, 1.589685, 1.271748, 1.017398, 0.813919, 0.651135], 'p_i': 40, 'u_i': 3.5196},
        {'id': 3, 'e_m': 9.849953, 'e_o_k': [3.737839, 2.990271, 2.392217, 1.913773, 1.531019, 1.224815], 'p_i': 80, 'u_i': 2.9192},
        {'id': 4, 'e_m': 1.498345, 'e_o_k': [0.710597, 0.568478, 0.454782, 0.363826], 'p_i': 40, 'u_i': 2.0454},
        {'id': 5, 'e_m': 0.680783, 'e_o_k': [0.258342, 0.206674, 0.165339, 0.132271, 0.105817, 0.084654], 'p_i': 40, 'u_i': 2.8602},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET
