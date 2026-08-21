"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120006, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120006, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.560098, 'e_o_k': [0.139228, 0.111383, 0.089106, 0.071285, 0.057028], 'p_i': 10, 'u_i': 2.3101},
        {'id': 1, 'e_m': 4.739356, 'e_o_k': [0.789893, 0.631914], 'p_i': 20, 'u_i': 1.0484},
        {'id': 2, 'e_m': 19.751983, 'e_o_k': [3.291997, 2.633598], 'p_i': 40, 'u_i': 3.4659},
        {'id': 3, 'e_m': 31.703866, 'e_o_k': [3.898016, 3.118413, 2.494730], 'p_i': 80, 'u_i': 2.7545},
        {'id': 4, 'e_m': 3.693150, 'e_o_k': [0.615525, 0.492420], 'p_i': 10, 'u_i': 4.1427},
        {'id': 5, 'e_m': 6.122700, 'e_o_k': [0.752791, 0.602233, 0.481786], 'p_i': 20, 'u_i': 2.5784},
        {'id': 6, 'e_m': 2.133681, 'e_o_k': [0.173504, 0.138803, 0.111042, 0.088834, 0.071067, 0.056854], 'p_i': 20, 'u_i': 2.4961},
        {'id': 7, 'e_m': 1.347904, 'e_o_k': [0.136982, 0.109586, 0.087669, 0.070135], 'p_i': 10, 'u_i': 4.2861},
    ]
    B_BUDGET = 263.120006
    return processors, tasks, B_BUDGET
