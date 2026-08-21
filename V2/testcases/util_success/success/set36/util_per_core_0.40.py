"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679997, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679997, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.942324, 'e_o_k': [0.084096, 0.067277, 0.053821, 0.043057, 0.034446], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.718592, 'e_o_k': [0.088351, 0.070681, 0.056545], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.754744, 'e_o_k': [0.061373, 0.049099, 0.039279, 0.031423, 0.025138, 0.020111], 'p_i': 40, 'u_i': 1.5166},
        {'id': 3, 'e_m': 4.113295, 'e_o_k': [0.685549, 0.548439], 'p_i': 80, 'u_i': 1.2517},
        {'id': 4, 'e_m': 15.892935, 'e_o_k': [1.615136, 1.292109, 1.033687, 0.826949], 'p_i': 40, 'u_i': 3.8216},
        {'id': 5, 'e_m': 3.188381, 'e_o_k': [0.392014, 0.313611, 0.250889], 'p_i': 40, 'u_i': 4.3612},
        {'id': 6, 'e_m': 1.051973, 'e_o_k': [0.106908, 0.085526, 0.068421, 0.054737], 'p_i': 10, 'u_i': 2.3108},
        {'id': 7, 'e_m': 0.692921, 'e_o_k': [0.070419, 0.056335, 0.045068, 0.036054], 'p_i': 40, 'u_i': 1.0383},
    ]
    B_BUDGET = 95.679997
    return processors, tasks, B_BUDGET
