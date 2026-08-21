"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 41.951999, "H": 80, "J": 31, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.1, "seed": 1025, "set": 25, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}
"""

_SPEC = '{"B": 41.951999, "H": 80, "J": 31, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.1, "seed": 1025, "set": 25, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.799720, 'e_o_k': [0.622004, 0.497604], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 2.592762, 'e_o_k': [1.487650, 1.190120, 0.952096], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 1.461112, 'e_o_k': [0.692939, 0.554351, 0.443481, 0.354785], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 3.792245, 'e_o_k': [2.949524, 2.359619], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 0.519494, 'e_o_k': [0.197136, 0.157709, 0.126167, 0.100934, 0.080747, 0.064598], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 0.710845, 'e_o_k': [0.269750, 0.215800, 0.172640, 0.138112, 0.110490, 0.088392], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 1.584893, 'e_o_k': [1.232695, 0.986156], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.183071, 'e_o_k': [0.105041, 0.084033, 0.067226], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 41.951999
    return processors, tasks, B_BUDGET
