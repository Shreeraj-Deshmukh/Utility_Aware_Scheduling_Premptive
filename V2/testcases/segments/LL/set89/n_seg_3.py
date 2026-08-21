"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199991, "H": 80, "J": 47, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199991, "H": 80, "J": 47, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.612231, 'e_o_k': [0.125457, 0.100366, 0.080293], 'p_i': 10, 'u_i': 3.9801},
        {'id': 1, 'e_m': 0.818720, 'e_o_k': [0.167771, 0.134216, 0.107373], 'p_i': 20, 'u_i': 3.7892},
        {'id': 2, 'e_m': 1.130553, 'e_o_k': [0.231671, 0.185337, 0.148269], 'p_i': 40, 'u_i': 1.4880},
        {'id': 3, 'e_m': 0.013730, 'e_o_k': [0.002814, 0.002251, 0.001801], 'p_i': 80, 'u_i': 4.5731},
        {'id': 4, 'e_m': 0.810047, 'e_o_k': [0.165993, 0.132795, 0.106236], 'p_i': 10, 'u_i': 3.7064},
        {'id': 5, 'e_m': 1.453435, 'e_o_k': [0.297835, 0.238268, 0.190614], 'p_i': 10, 'u_i': 4.7396},
        {'id': 6, 'e_m': 0.030685, 'e_o_k': [0.006288, 0.005030, 0.004024], 'p_i': 10, 'u_i': 4.0832},
        {'id': 7, 'e_m': 0.399887, 'e_o_k': [0.081944, 0.065555, 0.052444], 'p_i': 10, 'u_i': 1.4400},
    ]
    B_BUDGET = 55.199991
    return processors, tasks, B_BUDGET
