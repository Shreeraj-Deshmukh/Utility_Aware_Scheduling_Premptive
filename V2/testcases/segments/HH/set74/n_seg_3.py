"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.237773, 'e_o_k': [0.136427, 0.109142, 0.087313], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 2.303196, 'e_o_k': [1.321506, 1.057205, 0.845764], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 7.567437, 'e_o_k': [4.341972, 3.473578, 2.778862], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 20.093036, 'e_o_k': [11.528791, 9.223033, 7.378426], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.219572, 'e_o_k': [0.125984, 0.100787, 0.080630], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 9.972517, 'e_o_k': [5.721936, 4.577549, 3.662039], 'p_i': 80, 'u_i': 1.7696},
        {'id': 6, 'e_m': 3.107005, 'e_o_k': [1.782708, 1.426166, 1.140933], 'p_i': 80, 'u_i': 4.8086},
        {'id': 7, 'e_m': 0.705255, 'e_o_k': [0.404655, 0.323724, 0.258979], 'p_i': 20, 'u_i': 1.4894},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
