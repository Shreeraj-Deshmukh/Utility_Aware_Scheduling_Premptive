"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360001, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.118144, 'e_o_k': [0.099787, 0.079829, 0.063864, 0.051091, 0.040873], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 3.229963, 'e_o_k': [0.262650, 0.210120, 0.168096, 0.134477, 0.107581, 0.086065], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 12.716091, 'e_o_k': [1.563454, 1.250763, 1.000610], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 31.100788, 'e_o_k': [3.160649, 2.528519, 2.022815, 1.618252], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.007327, 'e_o_k': [0.001221, 0.000977], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 7.750588, 'e_o_k': [0.952941, 0.762353, 0.609882], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 1.445278, 'e_o_k': [0.146878, 0.117502, 0.094002, 0.075201], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 15.115299, 'e_o_k': [1.536108, 1.228886, 0.983109, 0.786487], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 191.360001
    return processors, tasks, B_BUDGET
