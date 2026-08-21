"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.419252, 'e_o_k': [1.103863, 0.883090], 'p_i': 10, 'u_i': 4.9667},
        {'id': 1, 'e_m': 0.182138, 'e_o_k': [0.075855, 0.060684, 0.048547, 0.038838, 0.031070], 'p_i': 20, 'u_i': 1.4132},
        {'id': 2, 'e_m': 0.741867, 'e_o_k': [0.425661, 0.340529, 0.272423], 'p_i': 40, 'u_i': 4.6321},
        {'id': 3, 'e_m': 0.220500, 'e_o_k': [0.091831, 0.073465, 0.058772, 0.047018, 0.037614], 'p_i': 80, 'u_i': 3.6983},
        {'id': 4, 'e_m': 2.936451, 'e_o_k': [1.222939, 0.978351, 0.782681, 0.626145, 0.500916], 'p_i': 20, 'u_i': 3.0670},
        {'id': 5, 'e_m': 6.467394, 'e_o_k': [5.030196, 4.024156], 'p_i': 80, 'u_i': 2.2547},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET
