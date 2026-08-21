"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.63998, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.63998, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067561, 'e_o_k': [0.612535, 0.490028, 0.392023], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 6.103602, 'e_o_k': [3.502067, 2.801653, 2.241323], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 4.537756, 'e_o_k': [2.603630, 2.082904, 1.666323], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 4.054946, 'e_o_k': [2.326608, 1.861287, 1.489029], 'p_i': 80, 'u_i': 2.9100},
        {'id': 4, 'e_m': 0.349178, 'e_o_k': [0.200348, 0.160279, 0.128223], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.690991, 'e_o_k': [0.396470, 0.317176, 0.253741], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 5.436589, 'e_o_k': [3.119355, 2.495484, 1.996387], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 2.776704, 'e_o_k': [1.593191, 1.274553, 1.019642], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 176.639980
    return processors, tasks, B_BUDGET
