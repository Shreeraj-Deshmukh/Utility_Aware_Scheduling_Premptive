"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.118887, 'e_o_k': [0.033024, 0.026419], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 1.151598, 'e_o_k': [0.319888, 0.255911], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 3.783719, 'e_o_k': [1.051033, 0.840826], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 10.046518, 'e_o_k': [2.790699, 2.232560], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.109786, 'e_o_k': [0.030496, 0.024397], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 4.986259, 'e_o_k': [1.385072, 1.108057], 'p_i': 80, 'u_i': 1.7696},
        {'id': 6, 'e_m': 1.553502, 'e_o_k': [0.431528, 0.345223], 'p_i': 80, 'u_i': 4.8086},
        {'id': 7, 'e_m': 0.352628, 'e_o_k': [0.097952, 0.078362], 'p_i': 20, 'u_i': 1.4894},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
