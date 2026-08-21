"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360018, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360018, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.564657, 'e_o_k': [0.260776, 0.208621], 'p_i': 10, 'u_i': 3.0961},
        {'id': 1, 'e_m': 3.820731, 'e_o_k': [0.388286, 0.310629, 0.248503, 0.198802], 'p_i': 20, 'u_i': 4.3282},
        {'id': 2, 'e_m': 4.624242, 'e_o_k': [0.770707, 0.616566], 'p_i': 40, 'u_i': 3.0285},
        {'id': 3, 'e_m': 16.846491, 'e_o_k': [1.712042, 1.369633, 1.095707, 0.876565], 'p_i': 80, 'u_i': 4.7214},
        {'id': 4, 'e_m': 0.138497, 'e_o_k': [0.017028, 0.013623, 0.010898], 'p_i': 20, 'u_i': 3.0081},
        {'id': 5, 'e_m': 2.263276, 'e_o_k': [0.377213, 0.301770], 'p_i': 10, 'u_i': 2.4883},
        {'id': 6, 'e_m': 4.475171, 'e_o_k': [0.363906, 0.291125, 0.232900, 0.186320, 0.149056, 0.119245], 'p_i': 10, 'u_i': 4.1387},
        {'id': 7, 'e_m': 2.455411, 'e_o_k': [0.219129, 0.175303, 0.140242, 0.112194, 0.089755], 'p_i': 10, 'u_i': 1.5889},
    ]
    B_BUDGET = 191.360018
    return processors, tasks, B_BUDGET
