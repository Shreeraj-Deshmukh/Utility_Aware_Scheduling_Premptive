"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400016, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.400016, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.970629, 'e_o_k': [0.210494, 0.126296, 0.075778, 0.045467, 0.027280], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 2.923011, 'e_o_k': [0.633894, 0.380336, 0.228202, 0.136921, 0.082153], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 1.109904, 'e_o_k': [0.255033, 0.153020, 0.091812, 0.055087], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 3.648613, 'e_o_k': [0.930769, 0.558461, 0.335077], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 1.035116, 'e_o_k': [0.264060, 0.158436, 0.095062], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 10.125219, 'e_o_k': [2.195788, 1.317473, 0.790484, 0.474290, 0.284574], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 4.891882, 'e_o_k': [1.247929, 0.748757, 0.449254], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.359380, 'e_o_k': [0.112306, 0.067384], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 110.400016
    return processors, tasks, B_BUDGET
