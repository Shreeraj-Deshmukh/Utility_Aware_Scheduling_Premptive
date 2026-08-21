"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.599170, 'e_o_k': [0.122781, 0.098225, 0.078580], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 4.185659, 'e_o_k': [0.857717, 0.686174, 0.548939], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.147250, 'e_o_k': [0.030174, 0.024139, 0.019311], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 1.074448, 'e_o_k': [0.220174, 0.176139, 0.140911], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.209273, 'e_o_k': [0.042884, 0.034307, 0.027446], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.141966, 'e_o_k': [0.029091, 0.023273, 0.018618], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.313697, 'e_o_k': [0.064282, 0.051426, 0.041141], 'p_i': 80, 'u_i': 4.3612},
        {'id': 7, 'e_m': 1.741302, 'e_o_k': [0.356824, 0.285459, 0.228367], 'p_i': 20, 'u_i': 4.6337},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
