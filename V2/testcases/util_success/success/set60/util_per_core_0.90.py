"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280012, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280012, "H": 80, "J": 39, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.888043, 'e_o_k': [0.257738, 0.206191, 0.164952, 0.131962, 0.105570], 'p_i': 10, 'u_i': 4.7898},
        {'id': 1, 'e_m': 9.293232, 'e_o_k': [0.829358, 0.663486, 0.530789, 0.424631, 0.339705], 'p_i': 20, 'u_i': 3.8151},
        {'id': 2, 'e_m': 2.730474, 'e_o_k': [0.277487, 0.221990, 0.177592, 0.142073], 'p_i': 40, 'u_i': 2.4922},
        {'id': 3, 'e_m': 11.720968, 'e_o_k': [0.953110, 0.762488, 0.609991, 0.487992, 0.390394, 0.312315], 'p_i': 80, 'u_i': 2.2134},
        {'id': 4, 'e_m': 5.094696, 'e_o_k': [0.626397, 0.501118, 0.400894], 'p_i': 20, 'u_i': 4.2486},
        {'id': 5, 'e_m': 0.920753, 'e_o_k': [0.074873, 0.059898, 0.047918, 0.038335, 0.030668, 0.024534], 'p_i': 10, 'u_i': 3.7555},
        {'id': 6, 'e_m': 4.440724, 'e_o_k': [0.740121, 0.592097], 'p_i': 20, 'u_i': 3.0652},
        {'id': 7, 'e_m': 2.629139, 'e_o_k': [0.438190, 0.350552], 'p_i': 10, 'u_i': 3.3025},
    ]
    B_BUDGET = 215.280012
    return processors, tasks, B_BUDGET
