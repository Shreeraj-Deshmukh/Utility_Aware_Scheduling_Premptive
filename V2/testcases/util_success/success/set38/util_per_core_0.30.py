"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759991, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759991, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.605893, 'e_o_k': [0.130586, 0.104469, 0.083575, 0.066860, 0.053488, 0.042790], 'p_i': 10, 'u_i': 1.2855},
        {'id': 1, 'e_m': 1.793883, 'e_o_k': [0.145873, 0.116698, 0.093358, 0.074687, 0.059749, 0.047800], 'p_i': 20, 'u_i': 4.6522},
        {'id': 2, 'e_m': 4.768881, 'e_o_k': [0.425590, 0.340472, 0.272378, 0.217902, 0.174322], 'p_i': 40, 'u_i': 4.9928},
        {'id': 3, 'e_m': 3.015374, 'e_o_k': [0.269102, 0.215281, 0.172225, 0.137780, 0.110224], 'p_i': 80, 'u_i': 3.9733},
        {'id': 4, 'e_m': 0.441761, 'e_o_k': [0.044894, 0.035915, 0.028732, 0.022986], 'p_i': 10, 'u_i': 1.2745},
        {'id': 5, 'e_m': 1.875127, 'e_o_k': [0.152479, 0.121983, 0.097587, 0.078069, 0.062455, 0.049964], 'p_i': 40, 'u_i': 2.7525},
        {'id': 6, 'e_m': 3.465565, 'e_o_k': [0.426094, 0.340875, 0.272700], 'p_i': 40, 'u_i': 3.5893},
        {'id': 7, 'e_m': 0.151090, 'e_o_k': [0.018577, 0.014861, 0.011889], 'p_i': 10, 'u_i': 2.8023},
    ]
    B_BUDGET = 71.759991
    return processors, tasks, B_BUDGET
