"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.340082, 'e_o_k': [0.206503, 0.123902, 0.074341, 0.044605, 0.026763], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 0.844927, 'e_o_k': [0.496315, 0.297789, 0.178673, 0.107204, 0.064322, 0.038593], 'p_i': 20, 'u_i': 1.5555},
        {'id': 2, 'e_m': 0.259808, 'e_o_k': [0.185577, 0.111346, 0.066808], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 9.047231, 'e_o_k': [7.916327, 4.749796], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 2.504897, 'e_o_k': [2.191785, 1.315071], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 0.977966, 'e_o_k': [0.629206, 0.377523, 0.226514, 0.135908], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 5.375256, 'e_o_k': [4.703349, 2.822009], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 2.099419, 'e_o_k': [1.350729, 0.810437, 0.486262, 0.291757], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET
