"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 41, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "freq", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 41, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "freq", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 1.0]},
        {'id': 1, 'frequencies': [0.4, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.920347, 'e_o_k': [1.108207, 0.886566, 0.709252, 0.567402, 0.453922, 0.363137], 'p_i': 10, 'u_i': 3.0949},
        {'id': 1, 'e_m': 0.834414, 'e_o_k': [0.478762, 0.383010, 0.306408], 'p_i': 20, 'u_i': 1.9752},
        {'id': 2, 'e_m': 4.634773, 'e_o_k': [1.930236, 1.544189, 1.235351, 0.988281, 0.790625], 'p_i': 40, 'u_i': 3.9662},
        {'id': 3, 'e_m': 0.634609, 'e_o_k': [0.364120, 0.291296, 0.233037], 'p_i': 80, 'u_i': 1.9890},
        {'id': 4, 'e_m': 3.457185, 'e_o_k': [1.439808, 1.151847, 0.921477, 0.737182, 0.589745], 'p_i': 40, 'u_i': 3.3639},
        {'id': 5, 'e_m': 0.421109, 'e_o_k': [0.199713, 0.159770, 0.127816, 0.102253], 'p_i': 10, 'u_i': 4.7869},
        {'id': 6, 'e_m': 0.414008, 'e_o_k': [0.196345, 0.157076, 0.125661, 0.100529], 'p_i': 10, 'u_i': 2.7944},
        {'id': 7, 'e_m': 1.725014, 'e_o_k': [1.341677, 1.073342], 'p_i': 10, 'u_i': 4.7769},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
