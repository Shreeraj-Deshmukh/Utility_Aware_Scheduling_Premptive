"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.418756, 'e_o_k': [0.325699, 0.260559], 'p_i': 10, 'u_i': 3.9687},
        {'id': 1, 'e_m': 0.250123, 'e_o_k': [0.194540, 0.155632], 'p_i': 20, 'u_i': 3.3202},
        {'id': 2, 'e_m': 5.305681, 'e_o_k': [4.126640, 3.301312], 'p_i': 40, 'u_i': 4.3833},
        {'id': 3, 'e_m': 3.803984, 'e_o_k': [2.958654, 2.366923], 'p_i': 80, 'u_i': 1.8853},
        {'id': 4, 'e_m': 1.413090, 'e_o_k': [1.099070, 0.879256], 'p_i': 20, 'u_i': 2.6679},
        {'id': 5, 'e_m': 0.064527, 'e_o_k': [0.050187, 0.040150], 'p_i': 10, 'u_i': 2.8390},
        {'id': 6, 'e_m': 0.594094, 'e_o_k': [0.462073, 0.369659], 'p_i': 40, 'u_i': 3.5794},
        {'id': 7, 'e_m': 2.938676, 'e_o_k': [2.285637, 1.828509], 'p_i': 40, 'u_i': 4.0478},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET
