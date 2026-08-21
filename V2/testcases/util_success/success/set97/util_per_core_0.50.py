"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600007, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600007, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.876641, 'e_o_k': [0.078234, 0.062587, 0.050070, 0.040056, 0.032045], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 8.576113, 'e_o_k': [1.054440, 0.843552, 0.674842], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.518249, 'e_o_k': [0.086375, 0.069100], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 4.287105, 'e_o_k': [0.348613, 0.278890, 0.223112, 0.178490, 0.142792, 0.114234], 'p_i': 80, 'u_i': 4.0993},
        {'id': 4, 'e_m': 1.748572, 'e_o_k': [0.291429, 0.233143], 'p_i': 20, 'u_i': 2.5958},
        {'id': 5, 'e_m': 6.868347, 'e_o_k': [0.844469, 0.675575, 0.540460], 'p_i': 80, 'u_i': 1.3643},
        {'id': 6, 'e_m': 6.378241, 'e_o_k': [0.518657, 0.414926, 0.331941, 0.265553, 0.212442, 0.169954], 'p_i': 40, 'u_i': 1.6218},
        {'id': 7, 'e_m': 6.739704, 'e_o_k': [0.684929, 0.547943, 0.438355, 0.350684], 'p_i': 80, 'u_i': 1.2955},
    ]
    B_BUDGET = 119.600007
    return processors, tasks, B_BUDGET
