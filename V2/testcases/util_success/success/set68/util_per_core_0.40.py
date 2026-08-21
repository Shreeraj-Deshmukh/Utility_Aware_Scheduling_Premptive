"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.68001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.68001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.930633, 'e_o_k': [0.155105, 0.124084], 'p_i': 10, 'u_i': 3.1458},
        {'id': 1, 'e_m': 3.264279, 'e_o_k': [0.331736, 0.265389, 0.212311, 0.169849], 'p_i': 20, 'u_i': 4.9683},
        {'id': 2, 'e_m': 2.777130, 'e_o_k': [0.462855, 0.370284], 'p_i': 40, 'u_i': 2.4718},
        {'id': 3, 'e_m': 8.264281, 'e_o_k': [0.672024, 0.537619, 0.430095, 0.344076, 0.275261, 0.220209], 'p_i': 80, 'u_i': 4.0774},
        {'id': 4, 'e_m': 2.998873, 'e_o_k': [0.243858, 0.195087, 0.156069, 0.124855, 0.099884, 0.079908], 'p_i': 80, 'u_i': 2.9703},
        {'id': 5, 'e_m': 0.395365, 'e_o_k': [0.035284, 0.028227, 0.022582, 0.018065, 0.014452], 'p_i': 40, 'u_i': 3.9269},
        {'id': 6, 'e_m': 2.545753, 'e_o_k': [0.424292, 0.339434], 'p_i': 10, 'u_i': 3.4836},
        {'id': 7, 'e_m': 2.761829, 'e_o_k': [0.246475, 0.197180, 0.157744, 0.126195, 0.100956], 'p_i': 40, 'u_i': 2.8974},
    ]
    B_BUDGET = 95.680010
    return processors, tasks, B_BUDGET
