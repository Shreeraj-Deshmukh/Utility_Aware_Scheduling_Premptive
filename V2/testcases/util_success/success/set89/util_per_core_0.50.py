"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599991, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599991, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.530578, 'e_o_k': [0.124461, 0.099569, 0.079655, 0.063724, 0.050979, 0.040784], 'p_i': 10, 'u_i': 1.1682},
        {'id': 1, 'e_m': 2.046801, 'e_o_k': [0.166439, 0.133151, 0.106521, 0.085217, 0.068173, 0.054539], 'p_i': 20, 'u_i': 1.7372},
        {'id': 2, 'e_m': 2.826383, 'e_o_k': [0.229832, 0.183866, 0.147093, 0.117674, 0.094139, 0.075311], 'p_i': 40, 'u_i': 1.2016},
        {'id': 3, 'e_m': 0.034326, 'e_o_k': [0.005721, 0.004577], 'p_i': 80, 'u_i': 4.7805},
        {'id': 4, 'e_m': 2.025118, 'e_o_k': [0.248990, 0.199192, 0.159354], 'p_i': 10, 'u_i': 3.7064},
        {'id': 5, 'e_m': 3.633588, 'e_o_k': [0.605598, 0.484478], 'p_i': 10, 'u_i': 4.7396},
        {'id': 6, 'e_m': 0.076713, 'e_o_k': [0.012785, 0.010228], 'p_i': 10, 'u_i': 4.0832},
        {'id': 7, 'e_m': 0.999717, 'e_o_k': [0.089218, 0.071374, 0.057099, 0.045680, 0.036544], 'p_i': 10, 'u_i': 1.4400},
    ]
    B_BUDGET = 119.599991
    return processors, tasks, B_BUDGET
