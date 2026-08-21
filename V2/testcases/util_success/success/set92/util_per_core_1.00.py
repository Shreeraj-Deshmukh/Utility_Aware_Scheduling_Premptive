"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200003, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200003, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.397680, 'e_o_k': [0.124733, 0.099787, 0.079829, 0.063864, 0.051091], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 4.037453, 'e_o_k': [0.328312, 0.262650, 0.210120, 0.168096, 0.134477, 0.107581], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 15.895113, 'e_o_k': [1.954317, 1.563454, 1.250763], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 38.875985, 'e_o_k': [3.950812, 3.160649, 2.528519, 2.022815], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.009159, 'e_o_k': [0.001527, 0.001221], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 9.688235, 'e_o_k': [1.191176, 0.952941, 0.762353], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 1.806598, 'e_o_k': [0.183597, 0.146878, 0.117502, 0.094002], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 18.894124, 'e_o_k': [1.920135, 1.536108, 1.228886, 0.983109], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 239.200003
    return processors, tasks, B_BUDGET
