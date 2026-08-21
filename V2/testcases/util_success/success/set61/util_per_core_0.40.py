"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680007, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680007, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.685913, 'e_o_k': [0.069707, 0.055765, 0.044612, 0.035690], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 2.484409, 'e_o_k': [0.252481, 0.201984, 0.161588, 0.129270], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.048071, 'e_o_k': [0.004290, 0.003432, 0.002746, 0.002196, 0.001757], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 11.321347, 'e_o_k': [1.150543, 0.920435, 0.736348, 0.589078], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 9.862979, 'e_o_k': [1.643830, 1.315064], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 3.207163, 'e_o_k': [0.286218, 0.228974, 0.183179, 0.146543, 0.117235], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 9.607054, 'e_o_k': [0.857364, 0.685891, 0.548713, 0.438971, 0.351176], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 1.410237, 'e_o_k': [0.143317, 0.114653, 0.091723, 0.073378], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 95.680007
    return processors, tasks, B_BUDGET
