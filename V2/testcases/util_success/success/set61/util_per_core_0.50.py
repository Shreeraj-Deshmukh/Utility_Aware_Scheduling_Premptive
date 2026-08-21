"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.857391, 'e_o_k': [0.087133, 0.069707, 0.055765, 0.044612], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 3.105511, 'e_o_k': [0.315601, 0.252481, 0.201984, 0.161588], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.060089, 'e_o_k': [0.005362, 0.004290, 0.003432, 0.002746, 0.002196], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 14.151684, 'e_o_k': [1.438179, 1.150543, 0.920435, 0.736348], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 12.328724, 'e_o_k': [2.054787, 1.643830], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 4.008954, 'e_o_k': [0.357772, 0.286218, 0.228974, 0.183179, 0.146543], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 12.008817, 'e_o_k': [1.071705, 0.857364, 0.685891, 0.548713, 0.438971], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 1.762796, 'e_o_k': [0.179146, 0.143317, 0.114653, 0.091723], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 119.600001
    return processors, tasks, B_BUDGET
