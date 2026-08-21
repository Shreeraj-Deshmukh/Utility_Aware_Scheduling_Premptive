"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.711602, 'e_o_k': [0.498121, 0.498121], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 1.956038, 'e_o_k': [0.456409, 0.456409, 0.456409, 0.456409, 0.456409, 0.456409], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 6.578908, 'e_o_k': [3.070157, 3.070157, 3.070157], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 14.898312, 'e_o_k': [6.952546, 6.952546, 6.952546], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 4.819102, 'e_o_k': [1.686686, 1.686686, 1.686686, 1.686686], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 0.459436, 'e_o_k': [0.107202, 0.107202, 0.107202, 0.107202, 0.107202, 0.107202], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 1.319662, 'e_o_k': [0.369505, 0.369505, 0.369505, 0.369505, 0.369505], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 2.163416, 'e_o_k': [1.514391, 1.514391], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET
