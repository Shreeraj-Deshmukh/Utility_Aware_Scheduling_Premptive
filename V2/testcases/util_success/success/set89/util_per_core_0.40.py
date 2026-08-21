"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679987, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679987, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.224462, 'e_o_k': [0.099569, 0.079655, 0.063724, 0.050979, 0.040784, 0.032627], 'p_i': 10, 'u_i': 1.1682},
        {'id': 1, 'e_m': 1.637441, 'e_o_k': [0.133151, 0.106521, 0.085217, 0.068173, 0.054539, 0.043631], 'p_i': 20, 'u_i': 1.7372},
        {'id': 2, 'e_m': 2.261107, 'e_o_k': [0.183866, 0.147093, 0.117674, 0.094139, 0.075311, 0.060249], 'p_i': 40, 'u_i': 1.2016},
        {'id': 3, 'e_m': 0.027461, 'e_o_k': [0.004577, 0.003661], 'p_i': 80, 'u_i': 4.7805},
        {'id': 4, 'e_m': 1.620094, 'e_o_k': [0.199192, 0.159354, 0.127483], 'p_i': 10, 'u_i': 3.7064},
        {'id': 5, 'e_m': 2.906870, 'e_o_k': [0.484478, 0.387583], 'p_i': 10, 'u_i': 4.7396},
        {'id': 6, 'e_m': 0.061370, 'e_o_k': [0.010228, 0.008183], 'p_i': 10, 'u_i': 4.0832},
        {'id': 7, 'e_m': 0.799773, 'e_o_k': [0.071374, 0.057099, 0.045680, 0.036544, 0.029235], 'p_i': 10, 'u_i': 1.4400},
    ]
    B_BUDGET = 95.679987
    return processors, tasks, B_BUDGET
