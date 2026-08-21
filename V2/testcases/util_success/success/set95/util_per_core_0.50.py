"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599991, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599991, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.979777, 'e_o_k': [0.201197, 0.160957, 0.128766, 0.103013], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 3.637734, 'e_o_k': [0.606289, 0.485031], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 8.529039, 'e_o_k': [0.693553, 0.554843, 0.443874, 0.355099, 0.284079, 0.227264], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 3.774589, 'e_o_k': [0.464089, 0.371271, 0.297017], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 4.895513, 'e_o_k': [0.398087, 0.318470, 0.254776, 0.203820, 0.163056, 0.130445], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 3.383082, 'e_o_k': [0.415953, 0.332762, 0.266210], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 10.289119, 'e_o_k': [0.918234, 0.734587, 0.587670, 0.470136, 0.376109], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 1.706845, 'e_o_k': [0.173460, 0.138768, 0.111014, 0.088811], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 119.599991
    return processors, tasks, B_BUDGET
