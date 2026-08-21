"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.201488, 'e_o_k': [0.122347, 0.073408, 0.044045, 0.026427, 0.015856], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.441830, 'e_o_k': [0.846939, 0.508164, 0.304898, 0.182939, 0.109763, 0.065858], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 8.661890, 'e_o_k': [7.579154, 4.547492], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 8.902172, 'e_o_k': [7.789401, 4.673641], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 5.993625, 'e_o_k': [5.244422, 3.146653], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 4.342413, 'e_o_k': [2.550759, 1.530456, 0.918273, 0.550964, 0.330578, 0.198347], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 1.301354, 'e_o_k': [1.138685, 0.683211], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 3.654332, 'e_o_k': [2.610237, 1.566142, 0.939685], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
