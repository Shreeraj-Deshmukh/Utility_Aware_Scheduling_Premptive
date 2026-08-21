"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400011, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400011, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.808019, 'e_o_k': [0.165578, 0.132462, 0.105970], 'p_i': 10, 'u_i': 4.1044},
        {'id': 1, 'e_m': 2.624685, 'e_o_k': [0.537845, 0.430276, 0.344221], 'p_i': 20, 'u_i': 3.5158},
        {'id': 2, 'e_m': 3.033921, 'e_o_k': [0.621705, 0.497364, 0.397891], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 20.140991, 'e_o_k': [4.127252, 3.301802, 2.641441], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 2.165693, 'e_o_k': [0.443790, 0.355032, 0.284025], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.136094, 'e_o_k': [0.027888, 0.022310, 0.017848], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 3.875810, 'e_o_k': [0.794223, 0.635379, 0.508303], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.483689, 'e_o_k': [0.099117, 0.079293, 0.063435], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 110.400011
    return processors, tasks, B_BUDGET
