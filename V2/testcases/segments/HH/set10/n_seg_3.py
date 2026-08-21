"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640022, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640022, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.443224, 'e_o_k': [0.254309, 0.203447, 0.162758], 'p_i': 10, 'u_i': 2.5678},
        {'id': 1, 'e_m': 0.385037, 'e_o_k': [0.220923, 0.176738, 0.141391], 'p_i': 20, 'u_i': 3.0744},
        {'id': 2, 'e_m': 7.186952, 'e_o_k': [4.123661, 3.298929, 2.639143], 'p_i': 40, 'u_i': 3.1102},
        {'id': 3, 'e_m': 20.620712, 'e_o_k': [11.831556, 9.465245, 7.572196], 'p_i': 80, 'u_i': 3.9862},
        {'id': 4, 'e_m': 1.451540, 'e_o_k': [0.832851, 0.666281, 0.533025], 'p_i': 20, 'u_i': 1.5757},
        {'id': 5, 'e_m': 1.346300, 'e_o_k': [0.772467, 0.617974, 0.494379], 'p_i': 10, 'u_i': 4.9941},
        {'id': 6, 'e_m': 2.067937, 'e_o_k': [1.186521, 0.949217, 0.759374], 'p_i': 40, 'u_i': 1.7632},
        {'id': 7, 'e_m': 1.603507, 'e_o_k': [0.920045, 0.736036, 0.588829], 'p_i': 40, 'u_i': 1.4284},
    ]
    B_BUDGET = 176.640022
    return processors, tasks, B_BUDGET
