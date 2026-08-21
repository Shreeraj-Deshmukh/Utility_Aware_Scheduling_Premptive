"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.051640, 'e_o_k': [0.014345, 0.011476], 'p_i': 10, 'u_i': 4.0574},
        {'id': 1, 'e_m': 2.466332, 'e_o_k': [0.685092, 0.548074], 'p_i': 20, 'u_i': 2.7090},
        {'id': 2, 'e_m': 3.747707, 'e_o_k': [1.041030, 0.832824], 'p_i': 40, 'u_i': 3.6072},
        {'id': 3, 'e_m': 4.153790, 'e_o_k': [1.153830, 0.923064], 'p_i': 80, 'u_i': 4.0494},
        {'id': 4, 'e_m': 0.386369, 'e_o_k': [0.107325, 0.085860], 'p_i': 20, 'u_i': 4.5815},
        {'id': 5, 'e_m': 4.381916, 'e_o_k': [1.217199, 0.973759], 'p_i': 20, 'u_i': 1.1362},
        {'id': 6, 'e_m': 1.777815, 'e_o_k': [0.493838, 0.395070], 'p_i': 80, 'u_i': 3.3217},
        {'id': 7, 'e_m': 10.610695, 'e_o_k': [2.947415, 2.357932], 'p_i': 40, 'u_i': 1.1761},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
