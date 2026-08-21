"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200013, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200013, "H": 80, "J": 20, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.340082, 'e_o_k': [0.069689, 0.055751, 0.044601], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 0.844927, 'e_o_k': [0.173141, 0.138513, 0.110810], 'p_i': 20, 'u_i': 2.4171},
        {'id': 2, 'e_m': 0.259808, 'e_o_k': [0.053239, 0.042591, 0.034073], 'p_i': 40, 'u_i': 4.5639},
        {'id': 3, 'e_m': 9.047231, 'e_o_k': [1.853941, 1.483153, 1.186522], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 2.504897, 'e_o_k': [0.513299, 0.410639, 0.328511], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 0.977966, 'e_o_k': [0.200403, 0.160322, 0.128258], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 5.375256, 'e_o_k': [1.101487, 0.881190, 0.704952], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 2.099419, 'e_o_k': [0.430209, 0.344167, 0.275334], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 55.200013
    return processors, tasks, B_BUDGET
