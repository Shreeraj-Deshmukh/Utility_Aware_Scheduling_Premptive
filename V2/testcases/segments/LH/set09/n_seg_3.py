"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.868614, 'e_o_k': [0.498385, 0.398708, 0.318966], 'p_i': 10, 'u_i': 1.8132},
        {'id': 1, 'e_m': 0.707032, 'e_o_k': [0.405674, 0.324539, 0.259631], 'p_i': 20, 'u_i': 3.6949},
        {'id': 2, 'e_m': 4.447481, 'e_o_k': [2.551833, 2.041467, 1.633173], 'p_i': 40, 'u_i': 3.0423},
        {'id': 3, 'e_m': 1.996160, 'e_o_k': [1.145338, 0.916270, 0.733016], 'p_i': 80, 'u_i': 3.2827},
        {'id': 4, 'e_m': 0.078011, 'e_o_k': [0.044760, 0.035808, 0.028647], 'p_i': 20, 'u_i': 1.0597},
        {'id': 5, 'e_m': 0.176089, 'e_o_k': [0.101035, 0.080828, 0.064662], 'p_i': 20, 'u_i': 4.4596},
        {'id': 6, 'e_m': 2.563544, 'e_o_k': [1.470886, 1.176709, 0.941367], 'p_i': 40, 'u_i': 4.8824},
        {'id': 7, 'e_m': 0.648544, 'e_o_k': [0.372116, 0.297692, 0.238154], 'p_i': 10, 'u_i': 1.5609},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
