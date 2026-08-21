"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200018, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200018, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.128317, 'e_o_k': [0.026295, 0.021036, 0.016829], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.270038, 'e_o_k': [0.055336, 0.044269, 0.035415], 'p_i': 20, 'u_i': 2.1078},
        {'id': 2, 'e_m': 0.379369, 'e_o_k': [0.077740, 0.062192, 0.049753], 'p_i': 40, 'u_i': 4.2406},
        {'id': 3, 'e_m': 8.098303, 'e_o_k': [1.659488, 1.327591, 1.062072], 'p_i': 80, 'u_i': 1.1754},
        {'id': 4, 'e_m': 5.065594, 'e_o_k': [1.038032, 0.830425, 0.664340], 'p_i': 40, 'u_i': 3.4237},
        {'id': 5, 'e_m': 3.042472, 'e_o_k': [0.623457, 0.498766, 0.399013], 'p_i': 40, 'u_i': 1.7653},
        {'id': 6, 'e_m': 0.412620, 'e_o_k': [0.084553, 0.067643, 0.054114], 'p_i': 10, 'u_i': 3.9977},
        {'id': 7, 'e_m': 0.379795, 'e_o_k': [0.077827, 0.062261, 0.049809], 'p_i': 20, 'u_i': 1.6134},
    ]
    B_BUDGET = 55.200018
    return processors, tasks, B_BUDGET
