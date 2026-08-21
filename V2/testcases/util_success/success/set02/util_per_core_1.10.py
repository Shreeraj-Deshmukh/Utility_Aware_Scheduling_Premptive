"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119998, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119998, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.807708, 'e_o_k': [0.801285, 0.641028], 'p_i': 10, 'u_i': 1.5179},
        {'id': 1, 'e_m': 4.899594, 'e_o_k': [0.602409, 0.481927, 0.385542], 'p_i': 20, 'u_i': 2.2792},
        {'id': 2, 'e_m': 13.884046, 'e_o_k': [1.239057, 0.991246, 0.792996, 0.634397, 0.507518], 'p_i': 40, 'u_i': 3.5560},
        {'id': 3, 'e_m': 32.253695, 'e_o_k': [3.277815, 2.622252, 2.097801, 1.678241], 'p_i': 80, 'u_i': 2.6712},
        {'id': 4, 'e_m': 4.513093, 'e_o_k': [0.366990, 0.293592, 0.234873, 0.187899, 0.150319, 0.120255], 'p_i': 40, 'u_i': 2.7352},
        {'id': 5, 'e_m': 1.508144, 'e_o_k': [0.134592, 0.107673, 0.086139, 0.068911, 0.055129], 'p_i': 20, 'u_i': 3.9664},
        {'id': 6, 'e_m': 3.023858, 'e_o_k': [0.307303, 0.245842, 0.196674, 0.157339], 'p_i': 10, 'u_i': 3.7211},
        {'id': 7, 'e_m': 2.333567, 'e_o_k': [0.237151, 0.189721, 0.151777, 0.121421], 'p_i': 10, 'u_i': 1.9870},
    ]
    B_BUDGET = 263.119998
    return processors, tasks, B_BUDGET
