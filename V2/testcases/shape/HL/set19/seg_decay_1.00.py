"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400025, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 110.400025, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.059421, 'e_o_k': [0.382428, 0.382428, 0.382428, 0.382428], 'p_i': 10, 'u_i': 1.9017},
        {'id': 1, 'e_m': 2.238024, 'e_o_k': [0.559506, 0.559506], 'p_i': 20, 'u_i': 4.1004},
        {'id': 2, 'e_m': 0.750637, 'e_o_k': [0.093830, 0.093830, 0.093830, 0.093830], 'p_i': 40, 'u_i': 2.6358},
        {'id': 3, 'e_m': 5.306501, 'e_o_k': [0.884417, 0.884417, 0.884417], 'p_i': 80, 'u_i': 4.3577},
        {'id': 4, 'e_m': 0.055926, 'e_o_k': [0.006991, 0.006991, 0.006991, 0.006991], 'p_i': 40, 'u_i': 4.2383},
        {'id': 5, 'e_m': 0.091009, 'e_o_k': [0.009101, 0.009101, 0.009101, 0.009101, 0.009101], 'p_i': 80, 'u_i': 1.1754},
        {'id': 6, 'e_m': 18.185686, 'e_o_k': [4.546421, 4.546421], 'p_i': 80, 'u_i': 2.9766},
        {'id': 7, 'e_m': 2.688109, 'e_o_k': [0.224009, 0.224009, 0.224009, 0.224009, 0.224009, 0.224009], 'p_i': 40, 'u_i': 4.8798},
    ]
    B_BUDGET = 110.400025
    return processors, tasks, B_BUDGET
