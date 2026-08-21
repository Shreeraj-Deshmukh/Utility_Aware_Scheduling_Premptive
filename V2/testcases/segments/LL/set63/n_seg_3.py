"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.823643, 'e_o_k': [0.168779, 0.135024, 0.108019], 'p_i': 10, 'u_i': 2.3752},
        {'id': 1, 'e_m': 0.017150, 'e_o_k': [0.003514, 0.002812, 0.002249], 'p_i': 20, 'u_i': 4.5040},
        {'id': 2, 'e_m': 1.462946, 'e_o_k': [0.299784, 0.239827, 0.191862], 'p_i': 40, 'u_i': 4.7123},
        {'id': 3, 'e_m': 0.827621, 'e_o_k': [0.169594, 0.135676, 0.108540], 'p_i': 80, 'u_i': 4.3702},
        {'id': 4, 'e_m': 0.489062, 'e_o_k': [0.100218, 0.080174, 0.064139], 'p_i': 20, 'u_i': 3.7678},
        {'id': 5, 'e_m': 0.934156, 'e_o_k': [0.191425, 0.153140, 0.122512], 'p_i': 40, 'u_i': 3.2312},
        {'id': 6, 'e_m': 7.716508, 'e_o_k': [1.581252, 1.265001, 1.012001], 'p_i': 80, 'u_i': 3.7207},
        {'id': 7, 'e_m': 5.023836, 'e_o_k': [1.029474, 0.823580, 0.658864], 'p_i': 40, 'u_i': 2.0745},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
