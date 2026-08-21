"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640013, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640013, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.320746, 'e_o_k': [0.133581, 0.106864, 0.085492, 0.068393, 0.054715], 'p_i': 10, 'u_i': 1.6464},
        {'id': 1, 'e_m': 2.479074, 'e_o_k': [1.928168, 1.542535], 'p_i': 20, 'u_i': 4.4830},
        {'id': 2, 'e_m': 6.943514, 'e_o_k': [2.634910, 2.107928, 1.686342, 1.349074, 1.079259, 0.863407], 'p_i': 40, 'u_i': 3.9048},
        {'id': 3, 'e_m': 8.482935, 'e_o_k': [3.532874, 2.826299, 2.261039, 1.808831, 1.447065], 'p_i': 80, 'u_i': 3.4604},
        {'id': 4, 'e_m': 4.344856, 'e_o_k': [2.492950, 1.994360, 1.595488], 'p_i': 20, 'u_i': 2.2645},
        {'id': 5, 'e_m': 1.471044, 'e_o_k': [0.612643, 0.490115, 0.392092, 0.313673, 0.250939], 'p_i': 10, 'u_i': 4.9290},
    ]
    B_BUDGET = 176.640013
    return processors, tasks, B_BUDGET
