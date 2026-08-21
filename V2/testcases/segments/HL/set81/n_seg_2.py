"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.808019, 'e_o_k': [0.224450, 0.179560], 'p_i': 10, 'u_i': 4.1044},
        {'id': 1, 'e_m': 2.624685, 'e_o_k': [0.729079, 0.583263], 'p_i': 20, 'u_i': 3.5158},
        {'id': 2, 'e_m': 3.033921, 'e_o_k': [0.842756, 0.674205], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 20.140991, 'e_o_k': [5.594720, 4.475776], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 2.165693, 'e_o_k': [0.601581, 0.481265], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.136094, 'e_o_k': [0.037804, 0.030243], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 3.875810, 'e_o_k': [1.076614, 0.861291], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.483689, 'e_o_k': [0.134358, 0.107486], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
