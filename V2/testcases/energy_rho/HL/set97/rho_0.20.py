"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 80.960003, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.2, "seed": 1097, "set": 97, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.20"}
"""

_SPEC = '{"B": 80.960003, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 0.2, "seed": 1097, "set": 97, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.20"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.701313, 'e_o_k': [0.104312, 0.083450, 0.066760, 0.053408, 0.042726], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 6.860890, 'e_o_k': [1.405920, 1.124736, 0.899789], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.414599, 'e_o_k': [0.115166, 0.092133], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 3.429684, 'e_o_k': [0.464817, 0.371854, 0.297483, 0.237987, 0.190389, 0.152311], 'p_i': 80, 'u_i': 4.0993},
        {'id': 4, 'e_m': 1.398858, 'e_o_k': [0.388572, 0.310857], 'p_i': 20, 'u_i': 2.5958},
        {'id': 5, 'e_m': 5.494678, 'e_o_k': [1.125959, 0.900767, 0.720613], 'p_i': 80, 'u_i': 1.3643},
        {'id': 6, 'e_m': 5.102592, 'e_o_k': [0.691543, 0.553235, 0.442588, 0.354070, 0.283256, 0.226605], 'p_i': 40, 'u_i': 1.6218},
        {'id': 7, 'e_m': 5.391763, 'e_o_k': [0.913239, 0.730591, 0.584473, 0.467578], 'p_i': 80, 'u_i': 1.2955},
    ]
    B_BUDGET = 80.960003
    return processors, tasks, B_BUDGET
