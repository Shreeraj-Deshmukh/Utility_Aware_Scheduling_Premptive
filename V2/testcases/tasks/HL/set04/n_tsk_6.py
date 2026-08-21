"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.270665, 'e_o_k': [0.215221, 0.172177, 0.137741, 0.110193], 'p_i': 10, 'u_i': 3.6021},
        {'id': 1, 'e_m': 0.081121, 'e_o_k': [0.016623, 0.013299, 0.010639], 'p_i': 20, 'u_i': 4.3808},
        {'id': 2, 'e_m': 4.023700, 'e_o_k': [0.681521, 0.545217, 0.436173, 0.348939], 'p_i': 40, 'u_i': 1.2748},
        {'id': 3, 'e_m': 7.615399, 'e_o_k': [1.560533, 1.248426, 0.998741], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 4.647066, 'e_o_k': [0.952268, 0.761814, 0.609451], 'p_i': 20, 'u_i': 3.8582},
        {'id': 5, 'e_m': 4.814784, 'e_o_k': [0.986636, 0.789309, 0.631447], 'p_i': 20, 'u_i': 1.6137},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
