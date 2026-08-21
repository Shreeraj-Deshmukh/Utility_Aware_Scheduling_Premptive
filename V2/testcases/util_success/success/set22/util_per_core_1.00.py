"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200003, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200003, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.039296, 'e_o_k': [0.247145, 0.197716, 0.158173, 0.126538, 0.101231, 0.080985], 'p_i': 10, 'u_i': 3.0520},
        {'id': 1, 'e_m': 0.332138, 'e_o_k': [0.040837, 0.032669, 0.026135], 'p_i': 20, 'u_i': 1.8188},
        {'id': 2, 'e_m': 5.864150, 'e_o_k': [0.977358, 0.781887], 'p_i': 40, 'u_i': 1.3467},
        {'id': 3, 'e_m': 10.892194, 'e_o_k': [0.885717, 0.708574, 0.566859, 0.453487, 0.362790, 0.290232], 'p_i': 80, 'u_i': 3.9525},
        {'id': 4, 'e_m': 3.108877, 'e_o_k': [0.315943, 0.252754, 0.202203, 0.161763], 'p_i': 10, 'u_i': 3.3005},
        {'id': 5, 'e_m': 4.437342, 'e_o_k': [0.396003, 0.316802, 0.253442, 0.202753, 0.162203], 'p_i': 10, 'u_i': 3.6474},
        {'id': 6, 'e_m': 3.000769, 'e_o_k': [0.304956, 0.243965, 0.195172, 0.156138], 'p_i': 10, 'u_i': 2.4979},
        {'id': 7, 'e_m': 6.840172, 'e_o_k': [0.695139, 0.556112, 0.444889, 0.355911], 'p_i': 20, 'u_i': 1.8465},
    ]
    B_BUDGET = 239.200003
    return processors, tasks, B_BUDGET
