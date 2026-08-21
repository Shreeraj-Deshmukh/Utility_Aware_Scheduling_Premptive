"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.109720, 'e_o_k': [0.062954, 0.050363, 0.040291], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 0.572679, 'e_o_k': [0.328586, 0.262869, 0.210295], 'p_i': 20, 'u_i': 3.8785},
        {'id': 2, 'e_m': 5.630863, 'e_o_k': [3.230823, 2.584658, 2.067727], 'p_i': 40, 'u_i': 2.8542},
        {'id': 3, 'e_m': 3.715241, 'e_o_k': [2.131696, 1.705357, 1.364285], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 1.331561, 'e_o_k': [0.764011, 0.611208, 0.488967], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 1.635691, 'e_o_k': [0.938511, 0.750809, 0.600647], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.014189, 'e_o_k': [0.008141, 0.006513, 0.005210], 'p_i': 40, 'u_i': 2.8369},
        {'id': 7, 'e_m': 0.653569, 'e_o_k': [0.374999, 0.299999, 0.239999], 'p_i': 10, 'u_i': 1.1432},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
