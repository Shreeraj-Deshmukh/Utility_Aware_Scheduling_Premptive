"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440003, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440003, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.454640, 'e_o_k': [0.046203, 0.036963, 0.029570, 0.023656], 'p_i': 10, 'u_i': 1.7775},
        {'id': 1, 'e_m': 8.441889, 'e_o_k': [1.406981, 1.125585], 'p_i': 20, 'u_i': 2.7606},
        {'id': 2, 'e_m': 2.794317, 'e_o_k': [0.227225, 0.181780, 0.145424, 0.116339, 0.093071, 0.074457], 'p_i': 40, 'u_i': 3.8298},
        {'id': 3, 'e_m': 35.032911, 'e_o_k': [3.126450, 2.501160, 2.000928, 1.600742, 1.280594], 'p_i': 80, 'u_i': 4.8992},
        {'id': 4, 'e_m': 0.131024, 'e_o_k': [0.011693, 0.009354, 0.007484, 0.005987, 0.004789], 'p_i': 20, 'u_i': 4.8891},
        {'id': 5, 'e_m': 0.311727, 'e_o_k': [0.051955, 0.041564], 'p_i': 20, 'u_i': 4.7769},
        {'id': 6, 'e_m': 15.337080, 'e_o_k': [1.558646, 1.246917, 0.997534, 0.798027], 'p_i': 80, 'u_i': 1.3167},
        {'id': 7, 'e_m': 16.865695, 'e_o_k': [2.073651, 1.658921, 1.327137], 'p_i': 80, 'u_i': 3.6826},
    ]
    B_BUDGET = 167.440003
    return processors, tasks, B_BUDGET
