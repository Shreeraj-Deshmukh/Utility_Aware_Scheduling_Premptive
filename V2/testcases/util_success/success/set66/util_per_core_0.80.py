"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360008, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360008, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.274573, 'e_o_k': [0.212429, 0.169943], 'p_i': 10, 'u_i': 4.4773},
        {'id': 1, 'e_m': 0.427961, 'e_o_k': [0.071327, 0.057061], 'p_i': 20, 'u_i': 2.4546},
        {'id': 2, 'e_m': 18.466248, 'e_o_k': [1.876651, 1.501321, 1.201057, 0.960845], 'p_i': 40, 'u_i': 1.1544},
        {'id': 3, 'e_m': 16.073740, 'e_o_k': [1.976280, 1.581024, 1.264819], 'p_i': 80, 'u_i': 4.0204},
        {'id': 4, 'e_m': 6.700151, 'e_o_k': [1.116692, 0.893353], 'p_i': 80, 'u_i': 3.1068},
        {'id': 5, 'e_m': 4.414127, 'e_o_k': [0.542720, 0.434176, 0.347341], 'p_i': 20, 'u_i': 4.2070},
        {'id': 6, 'e_m': 2.361072, 'e_o_k': [0.239946, 0.191957, 0.153566, 0.122853], 'p_i': 10, 'u_i': 1.7688},
        {'id': 7, 'e_m': 4.960027, 'e_o_k': [0.442649, 0.354119, 0.283295, 0.226636, 0.181309], 'p_i': 20, 'u_i': 4.8665},
    ]
    B_BUDGET = 191.360008
    return processors, tasks, B_BUDGET
