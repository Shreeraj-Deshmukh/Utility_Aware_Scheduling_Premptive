"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 20, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.340082, 'e_o_k': [0.034008, 0.034008, 0.034008, 0.034008, 0.034008], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 0.844927, 'e_o_k': [0.070411, 0.070411, 0.070411, 0.070411, 0.070411, 0.070411], 'p_i': 20, 'u_i': 1.5555},
        {'id': 2, 'e_m': 0.259808, 'e_o_k': [0.043301, 0.043301, 0.043301], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 9.047231, 'e_o_k': [2.261808, 2.261808], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 2.504897, 'e_o_k': [0.626224, 0.626224], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 0.977966, 'e_o_k': [0.122246, 0.122246, 0.122246, 0.122246], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 5.375256, 'e_o_k': [1.343814, 1.343814], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 2.099419, 'e_o_k': [0.262427, 0.262427, 0.262427, 0.262427], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
