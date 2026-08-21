"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.281059, 'e_o_k': [0.218602, 0.174881], 'p_i': 10, 'u_i': 4.6007},
        {'id': 1, 'e_m': 1.389833, 'e_o_k': [0.578821, 0.463057, 0.370446, 0.296357, 0.237085], 'p_i': 20, 'u_i': 4.4928},
        {'id': 2, 'e_m': 14.287523, 'e_o_k': [5.421798, 4.337439, 3.469951, 2.775961, 2.220769, 1.776615], 'p_i': 40, 'u_i': 4.0915},
        {'id': 3, 'e_m': 27.617149, 'e_o_k': [10.480096, 8.384077, 6.707261, 5.365809, 4.292647, 3.434118], 'p_i': 80, 'u_i': 4.3648},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET
