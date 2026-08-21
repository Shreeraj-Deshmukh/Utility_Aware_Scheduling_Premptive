"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.43999, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.43999, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.001270, 'e_o_k': [0.406633, 0.325307, 0.260245, 0.208196], 'p_i': 10, 'u_i': 1.7025},
        {'id': 1, 'e_m': 2.525671, 'e_o_k': [0.225399, 0.180319, 0.144255, 0.115404, 0.092323], 'p_i': 20, 'u_i': 2.0058},
        {'id': 2, 'e_m': 1.964253, 'e_o_k': [0.327375, 0.261900], 'p_i': 40, 'u_i': 3.5722},
        {'id': 3, 'e_m': 34.674984, 'e_o_k': [3.523880, 2.819104, 2.255283, 1.804227], 'p_i': 80, 'u_i': 1.2384},
        {'id': 4, 'e_m': 3.237150, 'e_o_k': [0.539525, 0.431620], 'p_i': 40, 'u_i': 4.5379},
        {'id': 5, 'e_m': 4.589836, 'e_o_k': [0.764973, 0.611978], 'p_i': 20, 'u_i': 1.9982},
        {'id': 6, 'e_m': 0.534657, 'e_o_k': [0.089109, 0.071288], 'p_i': 20, 'u_i': 2.1252},
        {'id': 7, 'e_m': 4.311392, 'e_o_k': [0.438150, 0.350520, 0.280416, 0.224333], 'p_i': 80, 'u_i': 4.2384},
    ]
    B_BUDGET = 167.439990
    return processors, tasks, B_BUDGET
