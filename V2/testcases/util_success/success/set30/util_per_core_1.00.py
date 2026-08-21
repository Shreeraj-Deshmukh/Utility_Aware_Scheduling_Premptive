"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200006, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200006, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.098237, 'e_o_k': [0.007988, 0.006391, 0.005112, 0.004090, 0.003272, 0.002618], 'p_i': 10, 'u_i': 1.5318},
        {'id': 1, 'e_m': 4.614284, 'e_o_k': [0.411794, 0.329435, 0.263548, 0.210838, 0.168671], 'p_i': 20, 'u_i': 1.6728},
        {'id': 2, 'e_m': 12.490696, 'e_o_k': [2.081783, 1.665426], 'p_i': 40, 'u_i': 2.2189},
        {'id': 3, 'e_m': 39.238348, 'e_o_k': [3.501756, 2.801405, 2.241124, 1.792899, 1.434319], 'p_i': 80, 'u_i': 1.2299},
        {'id': 4, 'e_m': 5.730595, 'e_o_k': [0.704581, 0.563665, 0.450932], 'p_i': 20, 'u_i': 3.9422},
        {'id': 5, 'e_m': 0.692979, 'e_o_k': [0.061844, 0.049475, 0.039580, 0.031664, 0.025331], 'p_i': 40, 'u_i': 1.8634},
        {'id': 6, 'e_m': 7.524422, 'e_o_k': [0.671504, 0.537203, 0.429762, 0.343810, 0.275048], 'p_i': 40, 'u_i': 1.0271},
        {'id': 7, 'e_m': 9.295012, 'e_o_k': [0.755840, 0.604672, 0.483737, 0.386990, 0.309592, 0.247673], 'p_i': 20, 'u_i': 2.3651},
    ]
    B_BUDGET = 239.200006
    return processors, tasks, B_BUDGET
