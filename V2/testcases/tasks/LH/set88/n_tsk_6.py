"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.472186, 'e_o_k': [0.223936, 0.179149, 0.143319, 0.114655], 'p_i': 10, 'u_i': 3.1874},
        {'id': 1, 'e_m': 1.113643, 'e_o_k': [0.866167, 0.692934], 'p_i': 20, 'u_i': 2.4550},
        {'id': 2, 'e_m': 3.618489, 'e_o_k': [2.076182, 1.660946, 1.328757], 'p_i': 40, 'u_i': 4.1368},
        {'id': 3, 'e_m': 0.177419, 'e_o_k': [0.137993, 0.110394], 'p_i': 80, 'u_i': 2.0023},
        {'id': 4, 'e_m': 7.030740, 'e_o_k': [2.928080, 2.342464, 1.873972, 1.499177, 1.199342], 'p_i': 40, 'u_i': 1.7941},
        {'id': 5, 'e_m': 1.146032, 'e_o_k': [0.477286, 0.381829, 0.305463, 0.244370, 0.195496], 'p_i': 40, 'u_i': 1.7354},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET
