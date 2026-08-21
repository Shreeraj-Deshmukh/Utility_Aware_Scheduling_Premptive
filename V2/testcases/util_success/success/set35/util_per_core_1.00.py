"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.788647, 'e_o_k': [0.308080, 0.246464, 0.197171, 0.157737, 0.126190, 0.100952], 'p_i': 10, 'u_i': 3.9981},
        {'id': 1, 'e_m': 6.893273, 'e_o_k': [0.700536, 0.560429, 0.448343, 0.358674], 'p_i': 20, 'u_i': 1.1221},
        {'id': 2, 'e_m': 9.916837, 'e_o_k': [1.219283, 0.975427, 0.780341], 'p_i': 40, 'u_i': 1.0173},
        {'id': 3, 'e_m': 21.216719, 'e_o_k': [3.536120, 2.828896], 'p_i': 80, 'u_i': 4.7591},
        {'id': 4, 'e_m': 9.880289, 'e_o_k': [1.004094, 0.803276, 0.642620, 0.514096], 'p_i': 80, 'u_i': 4.6573},
        {'id': 5, 'e_m': 26.198347, 'e_o_k': [3.221108, 2.576887, 2.061509], 'p_i': 80, 'u_i': 3.1574},
        {'id': 6, 'e_m': 2.627594, 'e_o_k': [0.213667, 0.170934, 0.136747, 0.109398, 0.087518, 0.070014], 'p_i': 10, 'u_i': 2.6010},
        {'id': 7, 'e_m': 0.991988, 'e_o_k': [0.121966, 0.097573, 0.078058], 'p_i': 20, 'u_i': 2.4102},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET
