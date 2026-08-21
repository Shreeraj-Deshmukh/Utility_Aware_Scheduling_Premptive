"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.496829, 'e_o_k': [0.082805, 0.066244], 'p_i': 10, 'u_i': 1.3417},
        {'id': 1, 'e_m': 6.997359, 'e_o_k': [0.860331, 0.688265, 0.550612], 'p_i': 20, 'u_i': 1.8511},
        {'id': 2, 'e_m': 12.820835, 'e_o_k': [1.144173, 0.915338, 0.732270, 0.585816, 0.468653], 'p_i': 40, 'u_i': 4.0269},
        {'id': 3, 'e_m': 23.850452, 'e_o_k': [3.975075, 3.180060], 'p_i': 80, 'u_i': 1.9345},
        {'id': 4, 'e_m': 9.078530, 'e_o_k': [1.513088, 1.210471], 'p_i': 20, 'u_i': 3.7416},
        {'id': 5, 'e_m': 35.976518, 'e_o_k': [4.423342, 3.538674, 2.830939], 'p_i': 80, 'u_i': 1.3128},
        {'id': 6, 'e_m': 2.069143, 'e_o_k': [0.254403, 0.203522, 0.162818], 'p_i': 10, 'u_i': 1.5894},
        {'id': 7, 'e_m': 5.700025, 'e_o_k': [0.463507, 0.370806, 0.296645, 0.237316, 0.189852, 0.151882], 'p_i': 80, 'u_i': 3.8422},
    ]
    B_BUDGET = 263.119999
    return processors, tasks, B_BUDGET
