"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.711602, 'e_o_k': [0.120529, 0.096423, 0.077138, 0.061711], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 1.956038, 'e_o_k': [0.331307, 0.265046, 0.212037, 0.169629], 'p_i': 20, 'u_i': 4.0273},
        {'id': 2, 'e_m': 6.578908, 'e_o_k': [1.114314, 0.891451, 0.713161, 0.570529], 'p_i': 40, 'u_i': 2.2476},
        {'id': 3, 'e_m': 14.898312, 'e_o_k': [2.523427, 2.018741, 1.614993, 1.291995], 'p_i': 80, 'u_i': 1.3199},
        {'id': 4, 'e_m': 4.819102, 'e_o_k': [0.816244, 0.652995, 0.522396, 0.417917], 'p_i': 80, 'u_i': 3.4892},
        {'id': 5, 'e_m': 0.459436, 'e_o_k': [0.077818, 0.062254, 0.049803, 0.039843], 'p_i': 10, 'u_i': 1.4050},
        {'id': 6, 'e_m': 1.319662, 'e_o_k': [0.223520, 0.178816, 0.143053, 0.114442], 'p_i': 20, 'u_i': 3.5798},
        {'id': 7, 'e_m': 2.163416, 'e_o_k': [0.366432, 0.293146, 0.234517, 0.187613], 'p_i': 20, 'u_i': 2.2529},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
