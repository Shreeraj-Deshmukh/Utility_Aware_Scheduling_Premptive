"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.964311, 'e_o_k': [0.401605, 0.321284, 0.257027, 0.205622, 0.164497], 'p_i': 10, 'u_i': 3.2309},
        {'id': 1, 'e_m': 8.642127, 'e_o_k': [3.599172, 2.879338, 2.303470, 1.842776, 1.474221], 'p_i': 20, 'u_i': 2.9440},
        {'id': 2, 'e_m': 0.480580, 'e_o_k': [0.275742, 0.220594, 0.176475], 'p_i': 40, 'u_i': 1.5741},
        {'id': 3, 'e_m': 4.458164, 'e_o_k': [1.691774, 1.353420, 1.082736, 0.866188, 0.692951, 0.554361], 'p_i': 80, 'u_i': 1.4817},
        {'id': 4, 'e_m': 4.126083, 'e_o_k': [3.209176, 2.567340], 'p_i': 40, 'u_i': 3.4660},
        {'id': 5, 'e_m': 2.011380, 'e_o_k': [0.763274, 0.610619, 0.488495, 0.390796, 0.312637, 0.250110], 'p_i': 20, 'u_i': 3.9304},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
