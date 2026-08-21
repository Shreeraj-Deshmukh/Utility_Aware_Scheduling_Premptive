"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.793526, 'e_o_k': [0.162608, 0.130086, 0.104069], 'p_i': 10, 'u_i': 3.3143},
        {'id': 1, 'e_m': 1.049928, 'e_o_k': [0.215149, 0.172119, 0.137696], 'p_i': 20, 'u_i': 3.2246},
        {'id': 2, 'e_m': 7.537585, 'e_o_k': [1.544587, 1.235670, 0.988536], 'p_i': 40, 'u_i': 4.6504},
        {'id': 3, 'e_m': 17.122126, 'e_o_k': [3.508632, 2.806906, 2.245525], 'p_i': 80, 'u_i': 4.9346},
        {'id': 4, 'e_m': 0.854071, 'e_o_k': [0.175015, 0.140012, 0.112009], 'p_i': 10, 'u_i': 2.0105},
        {'id': 5, 'e_m': 3.312634, 'e_o_k': [0.678818, 0.543055, 0.434444], 'p_i': 40, 'u_i': 3.0068},
        {'id': 6, 'e_m': 1.838787, 'e_o_k': [0.376801, 0.301440, 0.241152], 'p_i': 80, 'u_i': 1.6248},
        {'id': 7, 'e_m': 5.958164, 'e_o_k': [1.220935, 0.976748, 0.781399], 'p_i': 80, 'u_i': 2.1190},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET
