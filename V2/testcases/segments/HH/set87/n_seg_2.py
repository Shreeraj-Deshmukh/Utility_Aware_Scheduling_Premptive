"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.644057, 'e_o_k': [1.278711, 1.022969], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.317213, 'e_o_k': [0.246721, 0.197377], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 1.169415, 'e_o_k': [0.909545, 0.727636], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 12.303905, 'e_o_k': [9.569704, 7.655763], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 2.417694, 'e_o_k': [1.880429, 1.504343], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 1.761783, 'e_o_k': [1.370276, 1.096221], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 1.036762, 'e_o_k': [0.806371, 0.645097], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 2.274347, 'e_o_k': [1.768936, 1.415149], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET
