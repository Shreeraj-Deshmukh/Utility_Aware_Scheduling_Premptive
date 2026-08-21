"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359992, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359992, "H": 80, "J": 47, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.508508, 'e_o_k': [0.084751, 0.067801], 'p_i': 10, 'u_i': 2.4482},
        {'id': 1, 'e_m': 9.794696, 'e_o_k': [0.995396, 0.796317, 0.637053, 0.509643], 'p_i': 20, 'u_i': 4.8654},
        {'id': 2, 'e_m': 13.186948, 'e_o_k': [2.197825, 1.758260], 'p_i': 40, 'u_i': 2.4832},
        {'id': 3, 'e_m': 9.940623, 'e_o_k': [1.010226, 0.808181, 0.646545, 0.517236], 'p_i': 80, 'u_i': 1.7299},
        {'id': 4, 'e_m': 0.591119, 'e_o_k': [0.072679, 0.058143, 0.046514], 'p_i': 10, 'u_i': 4.6595},
        {'id': 5, 'e_m': 0.446638, 'e_o_k': [0.045390, 0.036312, 0.029050, 0.023240], 'p_i': 10, 'u_i': 1.6443},
        {'id': 6, 'e_m': 3.275348, 'e_o_k': [0.545891, 0.436713], 'p_i': 10, 'u_i': 1.9160},
        {'id': 7, 'e_m': 1.741723, 'e_o_k': [0.141631, 0.113305, 0.090644, 0.072515, 0.058012, 0.046410], 'p_i': 10, 'u_i': 1.4840},
    ]
    B_BUDGET = 191.359992
    return processors, tasks, B_BUDGET
