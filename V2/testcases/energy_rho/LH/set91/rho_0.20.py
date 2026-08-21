"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 47.104, "H": 80, "J": 27, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.2, "seed": 1091, "set": 91, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.20"}
"""

_SPEC = '{"B": 47.104, "H": 80, "J": 27, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.2, "seed": 1091, "set": 91, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.20"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.543832, 'e_o_k': [0.422980, 0.338384], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.195966, 'e_o_k': [0.092938, 0.074350, 0.059480, 0.047584], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 6.548072, 'e_o_k': [3.105454, 2.484363, 1.987491, 1.589993], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 3.827555, 'e_o_k': [2.976987, 2.381590], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.151912, 'e_o_k': [0.057647, 0.046118, 0.036894, 0.029515, 0.023612, 0.018890], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.377358, 'e_o_k': [0.178964, 0.143171, 0.114537, 0.091630], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 2.516575, 'e_o_k': [1.193498, 0.954798, 0.763839, 0.611071], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 1.395776, 'e_o_k': [0.800855, 0.640684, 0.512547], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 47.104000
    return processors, tasks, B_BUDGET
