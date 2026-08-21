"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.711602, 'e_o_k': [0.408296, 0.326637, 0.261310], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 1.956038, 'e_o_k': [1.122317, 0.897854, 0.718283], 'p_i': 20, 'u_i': 4.0273},
        {'id': 2, 'e_m': 6.578908, 'e_o_k': [3.774783, 3.019827, 2.415861], 'p_i': 40, 'u_i': 2.2476},
        {'id': 3, 'e_m': 14.898312, 'e_o_k': [8.548212, 6.838569, 5.470855], 'p_i': 80, 'u_i': 1.3199},
        {'id': 4, 'e_m': 4.819102, 'e_o_k': [2.765059, 2.212047, 1.769637], 'p_i': 80, 'u_i': 3.4892},
        {'id': 5, 'e_m': 0.459436, 'e_o_k': [0.263611, 0.210889, 0.168711], 'p_i': 10, 'u_i': 1.4050},
        {'id': 6, 'e_m': 1.319662, 'e_o_k': [0.757183, 0.605747, 0.484597], 'p_i': 20, 'u_i': 3.5798},
        {'id': 7, 'e_m': 2.163416, 'e_o_k': [1.241304, 0.993043, 0.794435], 'p_i': 20, 'u_i': 2.2529},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
