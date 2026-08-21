"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519988, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519988, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.072289, 'e_o_k': [0.008888, 0.007110, 0.005688], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 5.472077, 'e_o_k': [0.672796, 0.538237, 0.430590], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 8.418324, 'e_o_k': [1.035040, 0.828032, 0.662425], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 1.444866, 'e_o_k': [0.240811, 0.192649], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 8.165176, 'e_o_k': [0.728687, 0.582949, 0.466359, 0.373088, 0.298470], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 2.043929, 'e_o_k': [0.182407, 0.145925, 0.116740, 0.093392, 0.074714], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 1.838878, 'e_o_k': [0.306480, 0.245184], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 4.400853, 'e_o_k': [0.447241, 0.357793, 0.286234, 0.228987], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 143.519988
    return processors, tasks, B_BUDGET
