"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.68, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.68, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.094835, 'e_o_k': [0.111264, 0.089011, 0.071209, 0.056967], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 6.015361, 'e_o_k': [0.739594, 0.591675, 0.473340], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 1.364859, 'e_o_k': [0.110986, 0.088789, 0.071031, 0.056825, 0.045460, 0.036368], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 1.209297, 'e_o_k': [0.148684, 0.118947, 0.095158], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 2.498208, 'e_o_k': [0.253883, 0.203106, 0.162485, 0.129988], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 0.889705, 'e_o_k': [0.109390, 0.087512, 0.070010], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.376895, 'e_o_k': [0.062816, 0.050253], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 5.337019, 'e_o_k': [0.889503, 0.711603], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 95.680000
    return processors, tasks, B_BUDGET
