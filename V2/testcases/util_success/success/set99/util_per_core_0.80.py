"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360005, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360005, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.040710, 'e_o_k': [0.127956, 0.102365, 0.081892], 'p_i': 10, 'u_i': 2.4453},
        {'id': 1, 'e_m': 1.595381, 'e_o_k': [0.142377, 0.113902, 0.091121, 0.072897, 0.058318], 'p_i': 20, 'u_i': 4.4841},
        {'id': 2, 'e_m': 1.046669, 'e_o_k': [0.128689, 0.102951, 0.082361], 'p_i': 40, 'u_i': 2.2759},
        {'id': 3, 'e_m': 29.333435, 'e_o_k': [4.888906, 3.911125], 'p_i': 80, 'u_i': 4.2544},
        {'id': 4, 'e_m': 4.977618, 'e_o_k': [0.505855, 0.404684, 0.323747, 0.258998], 'p_i': 20, 'u_i': 1.1205},
        {'id': 5, 'e_m': 11.266287, 'e_o_k': [1.385199, 1.108159, 0.886528], 'p_i': 40, 'u_i': 1.0704},
        {'id': 6, 'e_m': 6.864612, 'e_o_k': [0.558207, 0.446566, 0.357253, 0.285802, 0.228642, 0.182913], 'p_i': 20, 'u_i': 1.5805},
        {'id': 7, 'e_m': 5.982267, 'e_o_k': [0.997045, 0.797636], 'p_i': 40, 'u_i': 2.6610},
    ]
    B_BUDGET = 191.360005
    return processors, tasks, B_BUDGET
