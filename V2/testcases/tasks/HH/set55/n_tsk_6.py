"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.098894, 'e_o_k': [2.410251, 1.928201], 'p_i': 10, 'u_i': 3.3617},
        {'id': 1, 'e_m': 2.272895, 'e_o_k': [1.077931, 0.862345, 0.689876, 0.551901], 'p_i': 20, 'u_i': 3.9677},
        {'id': 2, 'e_m': 2.581905, 'e_o_k': [0.979776, 0.783821, 0.627056, 0.501645, 0.401316, 0.321053], 'p_i': 40, 'u_i': 4.5134},
        {'id': 3, 'e_m': 13.579784, 'e_o_k': [7.791679, 6.233343, 4.986675], 'p_i': 80, 'u_i': 4.5874},
        {'id': 4, 'e_m': 6.350547, 'e_o_k': [3.643756, 2.915005, 2.332004], 'p_i': 80, 'u_i': 2.7347},
        {'id': 5, 'e_m': 5.023126, 'e_o_k': [2.882122, 2.305697, 1.844558], 'p_i': 80, 'u_i': 4.9671},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET
