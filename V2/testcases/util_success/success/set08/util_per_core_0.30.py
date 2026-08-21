"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759993, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759993, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.535389, 'e_o_k': [0.043536, 0.034829, 0.027863, 0.022290, 0.017832, 0.014266], 'p_i': 10, 'u_i': 4.1639},
        {'id': 1, 'e_m': 0.077126, 'e_o_k': [0.007838, 0.006270, 0.005016, 0.004013], 'p_i': 20, 'u_i': 2.0315},
        {'id': 2, 'e_m': 4.209154, 'e_o_k': [0.375638, 0.300511, 0.240409, 0.192327, 0.153862], 'p_i': 40, 'u_i': 1.5871},
        {'id': 3, 'e_m': 2.891811, 'e_o_k': [0.481968, 0.385575], 'p_i': 80, 'u_i': 1.8711},
        {'id': 4, 'e_m': 0.205233, 'e_o_k': [0.034205, 0.027364], 'p_i': 20, 'u_i': 4.9538},
        {'id': 5, 'e_m': 3.032588, 'e_o_k': [0.270638, 0.216510, 0.173208, 0.138567, 0.110853], 'p_i': 10, 'u_i': 2.3994},
        {'id': 6, 'e_m': 1.188170, 'e_o_k': [0.198028, 0.158423], 'p_i': 40, 'u_i': 1.5904},
        {'id': 7, 'e_m': 0.580037, 'e_o_k': [0.071316, 0.057053, 0.045642], 'p_i': 10, 'u_i': 2.4893},
    ]
    B_BUDGET = 71.759993
    return processors, tasks, B_BUDGET
