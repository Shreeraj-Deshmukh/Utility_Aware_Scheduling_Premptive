"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.349516, 'e_o_k': [0.145562, 0.116450, 0.093160, 0.074528, 0.059622], 'p_i': 10, 'u_i': 3.1382},
        {'id': 1, 'e_m': 0.142173, 'e_o_k': [0.059211, 0.047368, 0.037895, 0.030316, 0.024253], 'p_i': 20, 'u_i': 3.0103},
        {'id': 2, 'e_m': 7.230513, 'e_o_k': [4.148655, 3.318924, 2.655139], 'p_i': 40, 'u_i': 3.7408},
        {'id': 3, 'e_m': 4.388003, 'e_o_k': [3.412891, 2.730313], 'p_i': 80, 'u_i': 2.8589},
        {'id': 4, 'e_m': 4.485140, 'e_o_k': [2.573441, 2.058753, 1.647002], 'p_i': 40, 'u_i': 2.7598},
        {'id': 5, 'e_m': 0.101984, 'e_o_k': [0.079321, 0.063457], 'p_i': 10, 'u_i': 2.0735},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
