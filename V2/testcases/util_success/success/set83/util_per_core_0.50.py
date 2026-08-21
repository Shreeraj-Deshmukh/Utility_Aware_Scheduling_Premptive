"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600006, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600006, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.967126, 'e_o_k': [0.175553, 0.140442, 0.112354, 0.089883, 0.071906], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 1.860879, 'e_o_k': [0.151321, 0.121056, 0.096845, 0.077476, 0.061981, 0.049585], 'p_i': 20, 'u_i': 1.3163},
        {'id': 2, 'e_m': 1.420112, 'e_o_k': [0.144320, 0.115456, 0.092365, 0.073892], 'p_i': 40, 'u_i': 1.2768},
        {'id': 3, 'e_m': 17.191424, 'e_o_k': [2.113700, 1.690960, 1.352768], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 7.477974, 'e_o_k': [0.919423, 0.735538, 0.588431], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.842515, 'e_o_k': [0.075189, 0.060151, 0.048121, 0.038497, 0.030797], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 1.109792, 'e_o_k': [0.184965, 0.147972], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 12.872176, 'e_o_k': [1.148754, 0.919004, 0.735203, 0.588162, 0.470530], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 119.600006
    return processors, tasks, B_BUDGET
