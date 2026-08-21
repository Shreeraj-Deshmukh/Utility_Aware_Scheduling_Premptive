"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.624601, 'e_o_k': [0.127992, 0.102394, 0.081915], 'p_i': 10, 'u_i': 1.9682},
        {'id': 1, 'e_m': 0.610894, 'e_o_k': [0.125183, 0.100147, 0.080117], 'p_i': 20, 'u_i': 4.1538},
        {'id': 2, 'e_m': 3.088315, 'e_o_k': [0.632851, 0.506281, 0.405025], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 4.046818, 'e_o_k': [0.829266, 0.663413, 0.530730], 'p_i': 80, 'u_i': 4.6912},
        {'id': 4, 'e_m': 0.371042, 'e_o_k': [0.076033, 0.060827, 0.048661], 'p_i': 40, 'u_i': 2.4684},
        {'id': 5, 'e_m': 3.248721, 'e_o_k': [0.665722, 0.532577, 0.426062], 'p_i': 40, 'u_i': 2.6468},
        {'id': 6, 'e_m': 0.378075, 'e_o_k': [0.077474, 0.061979, 0.049584], 'p_i': 20, 'u_i': 2.0597},
        {'id': 7, 'e_m': 5.584342, 'e_o_k': [1.144332, 0.915466, 0.732373], 'p_i': 80, 'u_i': 3.8347},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
