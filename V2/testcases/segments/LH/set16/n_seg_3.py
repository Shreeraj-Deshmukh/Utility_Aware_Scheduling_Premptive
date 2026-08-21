"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.536605, 'e_o_k': [0.307888, 0.246310, 0.197048], 'p_i': 10, 'u_i': 3.4396},
        {'id': 1, 'e_m': 1.004911, 'e_o_k': [0.576588, 0.461271, 0.369017], 'p_i': 20, 'u_i': 1.7213},
        {'id': 2, 'e_m': 2.250211, 'e_o_k': [1.291105, 1.032884, 0.826307], 'p_i': 40, 'u_i': 2.3007},
        {'id': 3, 'e_m': 2.587062, 'e_o_k': [1.484380, 1.187504, 0.950003], 'p_i': 80, 'u_i': 2.4667},
        {'id': 4, 'e_m': 2.270607, 'e_o_k': [1.302807, 1.042246, 0.833797], 'p_i': 80, 'u_i': 2.4016},
        {'id': 5, 'e_m': 0.342865, 'e_o_k': [0.196726, 0.157381, 0.125905], 'p_i': 10, 'u_i': 3.4602},
        {'id': 6, 'e_m': 7.548057, 'e_o_k': [4.330852, 3.464682, 2.771746], 'p_i': 80, 'u_i': 3.9709},
        {'id': 7, 'e_m': 4.038448, 'e_o_k': [2.317142, 1.853714, 1.482971], 'p_i': 80, 'u_i': 1.7339},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET
