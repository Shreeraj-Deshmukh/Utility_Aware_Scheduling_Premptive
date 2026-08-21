"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.162586, 'e_o_k': [0.157563, 0.126050, 0.100840, 0.080672, 0.064538, 0.051630], 'p_i': 10, 'u_i': 2.0153},
        {'id': 1, 'e_m': 4.654398, 'e_o_k': [0.692289, 0.553831, 0.443065, 0.354452, 0.283562], 'p_i': 20, 'u_i': 4.1190},
        {'id': 2, 'e_m': 0.750044, 'e_o_k': [0.153698, 0.122958, 0.098366], 'p_i': 40, 'u_i': 4.7975},
        {'id': 3, 'e_m': 2.581637, 'e_o_k': [0.349884, 0.279907, 0.223925, 0.179140, 0.143312, 0.114650], 'p_i': 80, 'u_i': 4.0424},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
