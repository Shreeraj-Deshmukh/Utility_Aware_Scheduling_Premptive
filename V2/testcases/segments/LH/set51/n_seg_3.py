"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.415588, 'e_o_k': [0.812223, 0.649778, 0.519823], 'p_i': 10, 'u_i': 2.5682},
        {'id': 1, 'e_m': 1.559525, 'e_o_k': [0.894810, 0.715848, 0.572678], 'p_i': 20, 'u_i': 2.9074},
        {'id': 2, 'e_m': 1.007726, 'e_o_k': [0.578204, 0.462563, 0.370050], 'p_i': 40, 'u_i': 4.2053},
        {'id': 3, 'e_m': 1.342241, 'e_o_k': [0.770138, 0.616111, 0.492889], 'p_i': 80, 'u_i': 2.1233},
        {'id': 4, 'e_m': 4.007853, 'e_o_k': [2.299588, 1.839670, 1.471736], 'p_i': 80, 'u_i': 2.8725},
        {'id': 5, 'e_m': 0.593098, 'e_o_k': [0.340302, 0.272242, 0.217793], 'p_i': 20, 'u_i': 1.8909},
        {'id': 6, 'e_m': 1.066826, 'e_o_k': [0.612113, 0.489691, 0.391753], 'p_i': 20, 'u_i': 4.9900},
        {'id': 7, 'e_m': 0.431948, 'e_o_k': [0.247839, 0.198271, 0.158617], 'p_i': 80, 'u_i': 1.9407},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
