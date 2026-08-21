"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.093681, 'e_o_k': [0.026022, 0.020818], 'p_i': 10, 'u_i': 2.6135},
        {'id': 1, 'e_m': 1.157605, 'e_o_k': [0.156888, 0.125510, 0.100408, 0.080327, 0.064261, 0.051409], 'p_i': 20, 'u_i': 2.8871},
        {'id': 2, 'e_m': 3.049632, 'e_o_k': [0.413310, 0.330648, 0.264518, 0.211615, 0.169292, 0.135433], 'p_i': 40, 'u_i': 2.4127},
        {'id': 3, 'e_m': 7.683118, 'e_o_k': [1.574409, 1.259528, 1.007622], 'p_i': 80, 'u_i': 1.2331},
        {'id': 4, 'e_m': 3.136282, 'e_o_k': [0.642681, 0.514145, 0.411316], 'p_i': 40, 'u_i': 3.8857},
        {'id': 5, 'e_m': 1.641297, 'e_o_k': [0.455916, 0.364733], 'p_i': 20, 'u_i': 4.4773},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
