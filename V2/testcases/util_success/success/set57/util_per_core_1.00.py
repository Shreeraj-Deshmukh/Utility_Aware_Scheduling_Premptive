"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200008, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200008, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.863730, 'e_o_k': [0.395502, 0.316402, 0.253122, 0.202497, 0.161998, 0.129598], 'p_i': 10, 'u_i': 1.7395},
        {'id': 1, 'e_m': 1.981280, 'e_o_k': [0.201350, 0.161080, 0.128864, 0.103091], 'p_i': 20, 'u_i': 4.1268},
        {'id': 2, 'e_m': 5.053036, 'e_o_k': [0.410896, 0.328717, 0.262973, 0.210379, 0.168303, 0.134642], 'p_i': 40, 'u_i': 3.4957},
        {'id': 3, 'e_m': 14.555461, 'e_o_k': [2.425910, 1.940728], 'p_i': 80, 'u_i': 1.5632},
        {'id': 4, 'e_m': 2.265401, 'e_o_k': [0.230224, 0.184179, 0.147343, 0.117875], 'p_i': 10, 'u_i': 1.1256},
        {'id': 5, 'e_m': 3.128669, 'e_o_k': [0.384672, 0.307738, 0.246190], 'p_i': 20, 'u_i': 3.2221},
        {'id': 6, 'e_m': 4.572840, 'e_o_k': [0.762140, 0.609712], 'p_i': 20, 'u_i': 4.7984},
        {'id': 7, 'e_m': 9.893566, 'e_o_k': [1.216422, 0.973138, 0.778510], 'p_i': 20, 'u_i': 4.6807},
    ]
    B_BUDGET = 239.200008
    return processors, tasks, B_BUDGET
