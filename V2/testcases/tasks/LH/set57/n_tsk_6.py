"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.140327, 'e_o_k': [0.109144, 0.087315], 'p_i': 10, 'u_i': 2.3979},
        {'id': 1, 'e_m': 1.045262, 'e_o_k': [0.812982, 0.650385], 'p_i': 20, 'u_i': 4.6396},
        {'id': 2, 'e_m': 6.086089, 'e_o_k': [2.534664, 2.027731, 1.622185, 1.297748, 1.038198], 'p_i': 40, 'u_i': 4.1139},
        {'id': 3, 'e_m': 5.835122, 'e_o_k': [2.214299, 1.771439, 1.417152, 1.133721, 0.906977, 0.725582], 'p_i': 80, 'u_i': 3.3967},
        {'id': 4, 'e_m': 6.759010, 'e_o_k': [5.257008, 4.205606], 'p_i': 80, 'u_i': 1.9449},
        {'id': 5, 'e_m': 0.965011, 'e_o_k': [0.750564, 0.600451], 'p_i': 40, 'u_i': 4.6056},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET
