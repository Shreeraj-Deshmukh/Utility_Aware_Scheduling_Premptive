"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 186.943996, "H": 80, "J": 31, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.1, "seed": 1025, "set": 25, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.10"}
"""

_SPEC = '{"B": 186.943996, "H": 80, "J": 31, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.1, "seed": 1025, "set": 25, "sweep": "energy_rho", "util_per_core": 0.4, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.599440, 'e_o_k': [1.244009, 0.995207], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 5.185523, 'e_o_k': [2.975300, 2.380240, 1.904192], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 2.922224, 'e_o_k': [1.385879, 1.108703, 0.886962, 0.709570], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 7.584490, 'e_o_k': [5.899048, 4.719239], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 1.038987, 'e_o_k': [0.394273, 0.315418, 0.252334, 0.201868, 0.161494, 0.129195], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 1.421690, 'e_o_k': [0.539500, 0.431600, 0.345280, 0.276224, 0.220979, 0.176783], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 3.169787, 'e_o_k': [2.465390, 1.972312], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.366143, 'e_o_k': [0.210082, 0.168065, 0.134452], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 186.943996
    return processors, tasks, B_BUDGET
