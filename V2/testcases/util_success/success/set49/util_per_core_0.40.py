"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679995, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679995, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.001859, 'e_o_k': [0.000310, 0.000248], 'p_i': 10, 'u_i': 1.4564},
        {'id': 1, 'e_m': 1.030212, 'e_o_k': [0.104696, 0.083757, 0.067006, 0.053605], 'p_i': 20, 'u_i': 1.4719},
        {'id': 2, 'e_m': 0.499974, 'e_o_k': [0.061472, 0.049178, 0.039342], 'p_i': 40, 'u_i': 1.0831},
        {'id': 3, 'e_m': 3.303812, 'e_o_k': [0.294843, 0.235874, 0.188699, 0.150960, 0.120768], 'p_i': 80, 'u_i': 3.5025},
        {'id': 4, 'e_m': 16.765688, 'e_o_k': [1.363330, 1.090664, 0.872531, 0.698025, 0.558420, 0.446736], 'p_i': 40, 'u_i': 3.4020},
        {'id': 5, 'e_m': 1.698548, 'e_o_k': [0.283091, 0.226473], 'p_i': 20, 'u_i': 4.4776},
        {'id': 6, 'e_m': 0.189483, 'e_o_k': [0.015408, 0.012326, 0.009861, 0.007889, 0.006311, 0.005049], 'p_i': 10, 'u_i': 3.0661},
        {'id': 7, 'e_m': 1.714886, 'e_o_k': [0.139449, 0.111559, 0.089247, 0.071398, 0.057118, 0.045695], 'p_i': 10, 'u_i': 2.9486},
    ]
    B_BUDGET = 95.679995
    return processors, tasks, B_BUDGET
