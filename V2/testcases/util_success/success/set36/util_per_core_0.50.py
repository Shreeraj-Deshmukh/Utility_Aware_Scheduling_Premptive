"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599991, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599991, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.177905, 'e_o_k': [0.105120, 0.084096, 0.067277, 0.053821, 0.043057], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.898240, 'e_o_k': [0.110439, 0.088351, 0.070681], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.943430, 'e_o_k': [0.076717, 0.061373, 0.049099, 0.039279, 0.031423, 0.025138], 'p_i': 40, 'u_i': 1.5166},
        {'id': 3, 'e_m': 5.141619, 'e_o_k': [0.856936, 0.685549], 'p_i': 80, 'u_i': 1.2517},
        {'id': 4, 'e_m': 19.866168, 'e_o_k': [2.018920, 1.615136, 1.292109, 1.033687], 'p_i': 40, 'u_i': 3.8216},
        {'id': 5, 'e_m': 3.985476, 'e_o_k': [0.490018, 0.392014, 0.313611], 'p_i': 40, 'u_i': 4.3612},
        {'id': 6, 'e_m': 1.314966, 'e_o_k': [0.133635, 0.106908, 0.085526, 0.068421], 'p_i': 10, 'u_i': 2.3108},
        {'id': 7, 'e_m': 0.866151, 'e_o_k': [0.088023, 0.070419, 0.056335, 0.045068], 'p_i': 40, 'u_i': 1.0383},
    ]
    B_BUDGET = 119.599991
    return processors, tasks, B_BUDGET
