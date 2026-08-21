"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024511, 'e_o_k': [0.014064, 0.011251, 0.009001], 'p_i': 10, 'u_i': 1.0223},
        {'id': 1, 'e_m': 1.054701, 'e_o_k': [0.605156, 0.484125, 0.387300], 'p_i': 20, 'u_i': 1.6533},
        {'id': 2, 'e_m': 1.348573, 'e_o_k': [0.773772, 0.619017, 0.495214], 'p_i': 40, 'u_i': 4.3793},
        {'id': 3, 'e_m': 2.496489, 'e_o_k': [1.432412, 1.145929, 0.916744], 'p_i': 80, 'u_i': 2.7000},
        {'id': 4, 'e_m': 9.549774, 'e_o_k': [5.479378, 4.383503, 3.506802], 'p_i': 80, 'u_i': 2.7208},
        {'id': 5, 'e_m': 0.041493, 'e_o_k': [0.023808, 0.019046, 0.015237], 'p_i': 10, 'u_i': 2.5904},
        {'id': 6, 'e_m': 0.729370, 'e_o_k': [0.418491, 0.334793, 0.267834], 'p_i': 80, 'u_i': 1.1735},
        {'id': 7, 'e_m': 2.945096, 'e_o_k': [1.689809, 1.351847, 1.081478], 'p_i': 20, 'u_i': 1.5807},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET
