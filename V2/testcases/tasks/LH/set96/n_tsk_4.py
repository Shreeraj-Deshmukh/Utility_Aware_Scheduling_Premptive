"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.565390, 'e_o_k': [0.235467, 0.188373, 0.150699, 0.120559, 0.096447], 'p_i': 10, 'u_i': 3.2031},
        {'id': 1, 'e_m': 0.264926, 'e_o_k': [0.125643, 0.100514, 0.080411, 0.064329], 'p_i': 20, 'u_i': 2.0803},
        {'id': 2, 'e_m': 11.606642, 'e_o_k': [4.833799, 3.867039, 3.093631, 2.474905, 1.979924], 'p_i': 40, 'u_i': 3.1382},
        {'id': 3, 'e_m': 3.203895, 'e_o_k': [1.334321, 1.067457, 0.853965, 0.683172, 0.546538], 'p_i': 80, 'u_i': 3.0103},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
