"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.072980, 'e_o_k': [1.612318, 1.289854], 'p_i': 10, 'u_i': 3.4158},
        {'id': 1, 'e_m': 0.396463, 'e_o_k': [0.308360, 0.246688], 'p_i': 20, 'u_i': 2.7668},
        {'id': 2, 'e_m': 1.417028, 'e_o_k': [0.813049, 0.650439, 0.520351], 'p_i': 40, 'u_i': 2.4237},
        {'id': 3, 'e_m': 10.996250, 'e_o_k': [4.172833, 3.338267, 2.670613, 2.136491, 1.709193, 1.367354], 'p_i': 80, 'u_i': 3.6832},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
