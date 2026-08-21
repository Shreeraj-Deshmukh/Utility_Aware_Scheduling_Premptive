"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.675362, 'e_o_k': [0.525281, 0.420225], 'p_i': 10, 'u_i': 2.3226},
        {'id': 1, 'e_m': 1.331439, 'e_o_k': [1.035564, 0.828451], 'p_i': 20, 'u_i': 1.3159},
        {'id': 2, 'e_m': 3.504342, 'e_o_k': [2.725599, 2.180479], 'p_i': 40, 'u_i': 2.3324},
        {'id': 3, 'e_m': 7.942253, 'e_o_k': [3.307697, 2.646157, 2.116926, 1.693541, 1.354833], 'p_i': 80, 'u_i': 2.7878},
        {'id': 4, 'e_m': 1.377209, 'e_o_k': [0.790202, 0.632162, 0.505729], 'p_i': 40, 'u_i': 1.7467},
        {'id': 5, 'e_m': 4.445749, 'e_o_k': [1.687063, 1.349651, 1.079721, 0.863776, 0.691021, 0.552817], 'p_i': 10, 'u_i': 1.9890},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
