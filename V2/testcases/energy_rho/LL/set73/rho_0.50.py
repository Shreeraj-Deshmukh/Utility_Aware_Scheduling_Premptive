"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 46.0, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1073, "set": 73, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}
"""

_SPEC = '{"B": 46.0, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.5, "seed": 1073, "set": 73, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.599170, 'e_o_k': [0.122781, 0.098225, 0.078580], 'p_i': 10, 'u_i': 3.9348},
        {'id': 1, 'e_m': 4.185659, 'e_o_k': [1.162683, 0.930146], 'p_i': 20, 'u_i': 2.2078},
        {'id': 2, 'e_m': 0.147250, 'e_o_k': [0.024941, 0.019953, 0.015962, 0.012770], 'p_i': 40, 'u_i': 1.5646},
        {'id': 3, 'e_m': 1.074448, 'e_o_k': [0.298458, 0.238766], 'p_i': 80, 'u_i': 4.4075},
        {'id': 4, 'e_m': 0.209273, 'e_o_k': [0.058131, 0.046505], 'p_i': 10, 'u_i': 2.2030},
        {'id': 5, 'e_m': 0.141966, 'e_o_k': [0.029091, 0.023273, 0.018618], 'p_i': 80, 'u_i': 2.4770},
        {'id': 6, 'e_m': 0.313697, 'e_o_k': [0.042515, 0.034012, 0.027209, 0.021767, 0.017414, 0.013931], 'p_i': 80, 'u_i': 1.9604},
        {'id': 7, 'e_m': 1.741302, 'e_o_k': [0.294936, 0.235949, 0.188759, 0.151007], 'p_i': 20, 'u_i': 2.4961},
    ]
    B_BUDGET = 46.000000
    return processors, tasks, B_BUDGET
