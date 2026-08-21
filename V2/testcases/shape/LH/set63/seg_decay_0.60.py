"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.823643, 'e_o_k': [0.483813, 0.290288, 0.174173, 0.104504, 0.062702, 0.037621], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.017150, 'e_o_k': [0.011034, 0.006620, 0.003972, 0.002383], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 1.462946, 'e_o_k': [1.280078, 0.768047], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 0.827621, 'e_o_k': [0.591158, 0.354695, 0.212817], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 0.489062, 'e_o_k': [0.296967, 0.178180, 0.106908, 0.064145, 0.038487], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 0.934156, 'e_o_k': [0.601020, 0.360612, 0.216367, 0.129820], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 7.716508, 'e_o_k': [4.964665, 2.978799, 1.787279, 1.072368], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 5.023836, 'e_o_k': [3.588454, 2.153072, 1.291843], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
