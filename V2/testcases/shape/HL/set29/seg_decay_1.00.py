"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.555176, 'e_o_k': [0.069397, 0.069397, 0.069397, 0.069397], 'p_i': 10, 'u_i': 2.4751},
        {'id': 1, 'e_m': 0.851460, 'e_o_k': [0.085146, 0.085146, 0.085146, 0.085146, 0.085146], 'p_i': 20, 'u_i': 3.6644},
        {'id': 2, 'e_m': 3.395703, 'e_o_k': [0.339570, 0.339570, 0.339570, 0.339570, 0.339570], 'p_i': 40, 'u_i': 2.2976},
        {'id': 3, 'e_m': 3.482314, 'e_o_k': [0.348231, 0.348231, 0.348231, 0.348231, 0.348231], 'p_i': 80, 'u_i': 4.8639},
        {'id': 4, 'e_m': 4.033383, 'e_o_k': [1.008346, 1.008346], 'p_i': 40, 'u_i': 4.5045},
        {'id': 5, 'e_m': 2.789347, 'e_o_k': [0.464891, 0.464891, 0.464891], 'p_i': 80, 'u_i': 1.0020},
        {'id': 6, 'e_m': 3.567276, 'e_o_k': [0.445910, 0.445910, 0.445910, 0.445910], 'p_i': 40, 'u_i': 4.9529},
        {'id': 7, 'e_m': 3.486046, 'e_o_k': [0.871512, 0.871512], 'p_i': 10, 'u_i': 2.3587},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET
