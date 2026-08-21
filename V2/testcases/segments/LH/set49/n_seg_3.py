"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.000930, 'e_o_k': [0.000533, 0.000427, 0.000341], 'p_i': 10, 'u_i': 1.4564},
        {'id': 1, 'e_m': 0.515106, 'e_o_k': [0.295553, 0.236442, 0.189154], 'p_i': 20, 'u_i': 1.4719},
        {'id': 2, 'e_m': 0.249987, 'e_o_k': [0.143435, 0.114748, 0.091798], 'p_i': 40, 'u_i': 1.0831},
        {'id': 3, 'e_m': 1.651906, 'e_o_k': [0.947815, 0.758252, 0.606602], 'p_i': 80, 'u_i': 3.5025},
        {'id': 4, 'e_m': 8.382844, 'e_o_k': [4.809829, 3.847863, 3.078290], 'p_i': 40, 'u_i': 4.4776},
        {'id': 5, 'e_m': 0.849274, 'e_o_k': [0.487288, 0.389831, 0.311865], 'p_i': 20, 'u_i': 3.2024},
        {'id': 6, 'e_m': 0.094741, 'e_o_k': [0.054360, 0.043488, 0.034790], 'p_i': 10, 'u_i': 1.4405},
        {'id': 7, 'e_m': 0.857443, 'e_o_k': [0.491975, 0.393580, 0.314864], 'p_i': 10, 'u_i': 3.4151},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET
