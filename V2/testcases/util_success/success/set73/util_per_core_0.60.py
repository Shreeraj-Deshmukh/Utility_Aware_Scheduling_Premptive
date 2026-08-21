"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519992, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519992, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.271698, 'e_o_k': [0.045283, 0.036226], 'p_i': 10, 'u_i': 4.4075},
        {'id': 1, 'e_m': 0.193616, 'e_o_k': [0.032269, 0.025815], 'p_i': 20, 'u_i': 2.2030},
        {'id': 2, 'e_m': 6.525787, 'e_o_k': [0.802351, 0.641881, 0.513505], 'p_i': 40, 'u_i': 2.4770},
        {'id': 3, 'e_m': 3.037056, 'e_o_k': [0.246963, 0.197571, 0.158057, 0.126445, 0.101156, 0.080925], 'p_i': 80, 'u_i': 1.9604},
        {'id': 4, 'e_m': 3.846915, 'e_o_k': [0.390947, 0.312757, 0.250206, 0.200165], 'p_i': 10, 'u_i': 2.4961},
        {'id': 5, 'e_m': 3.312497, 'e_o_k': [0.407274, 0.325819, 0.260656], 'p_i': 40, 'u_i': 1.0730},
        {'id': 6, 'e_m': 8.746852, 'e_o_k': [1.075433, 0.860346, 0.688277], 'p_i': 20, 'u_i': 2.7749},
        {'id': 7, 'e_m': 1.143899, 'e_o_k': [0.093018, 0.074414, 0.059532, 0.047625, 0.038100, 0.030480], 'p_i': 20, 'u_i': 1.2098},
    ]
    B_BUDGET = 143.519992
    return processors, tasks, B_BUDGET
