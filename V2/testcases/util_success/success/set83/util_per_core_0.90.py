"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279998, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279998, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.540827, 'e_o_k': [0.315995, 0.252796, 0.202237, 0.161789, 0.129431], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 3.349583, 'e_o_k': [0.272377, 0.217902, 0.174321, 0.139457, 0.111566, 0.089252], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 2.556202, 'e_o_k': [0.259777, 0.207821, 0.166257, 0.133006], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 30.944564, 'e_o_k': [3.804659, 3.043728, 2.434982], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 13.460353, 'e_o_k': [1.654961, 1.323969, 1.059175], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 1.516526, 'e_o_k': [0.135340, 0.108272, 0.086617, 0.069294, 0.055435], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 1.997626, 'e_o_k': [0.332938, 0.266350], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 23.169916, 'e_o_k': [2.067758, 1.654206, 1.323365, 1.058692, 0.846954], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 215.279998
    return processors, tasks, B_BUDGET
