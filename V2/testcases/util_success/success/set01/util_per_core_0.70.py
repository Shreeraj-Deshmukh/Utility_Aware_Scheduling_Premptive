"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440008, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440008, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.688614, 'e_o_k': [0.137312, 0.109850, 0.087880, 0.070304, 0.056243, 0.044995], 'p_i': 10, 'u_i': 4.5109},
        {'id': 1, 'e_m': 3.718248, 'e_o_k': [0.331828, 0.265463, 0.212370, 0.169896, 0.135917], 'p_i': 20, 'u_i': 3.7479},
        {'id': 2, 'e_m': 3.462813, 'e_o_k': [0.577136, 0.461708], 'p_i': 40, 'u_i': 4.4508},
        {'id': 3, 'e_m': 15.665977, 'e_o_k': [1.592071, 1.273657, 1.018925, 0.815140], 'p_i': 80, 'u_i': 2.7382},
        {'id': 4, 'e_m': 10.364941, 'e_o_k': [1.727490, 1.381992], 'p_i': 80, 'u_i': 3.1722},
        {'id': 5, 'e_m': 2.791314, 'e_o_k': [0.249106, 0.199285, 0.159428, 0.127542, 0.102034], 'p_i': 20, 'u_i': 1.3571},
        {'id': 6, 'e_m': 9.373223, 'e_o_k': [0.952563, 0.762051, 0.609641, 0.487712], 'p_i': 20, 'u_i': 1.6646},
        {'id': 7, 'e_m': 0.250426, 'e_o_k': [0.041738, 0.033390], 'p_i': 10, 'u_i': 1.5964},
    ]
    B_BUDGET = 167.440008
    return processors, tasks, B_BUDGET
