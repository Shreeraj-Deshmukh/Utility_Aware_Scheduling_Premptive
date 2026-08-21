"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.327677, 'e_o_k': [0.386216, 0.308973, 0.247178, 0.197743, 0.158194], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 4.093935, 'e_o_k': [0.332905, 0.266324, 0.213059, 0.170447, 0.136358, 0.109086], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 3.124247, 'e_o_k': [0.317505, 0.254004, 0.203203, 0.162562], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 37.821134, 'e_o_k': [4.650139, 3.720111, 2.976089], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 16.451542, 'e_o_k': [2.022731, 1.618184, 1.294548], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 1.853532, 'e_o_k': [0.165415, 0.132332, 0.105866, 0.084693, 0.067754], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 2.441543, 'e_o_k': [0.406924, 0.325539], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 28.318787, 'e_o_k': [2.527260, 2.021808, 1.617446, 1.293957, 1.035166], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 263.120001
    return processors, tasks, B_BUDGET
