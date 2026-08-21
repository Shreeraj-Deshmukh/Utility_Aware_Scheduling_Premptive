"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200016, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200016, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.070595, 'e_o_k': [0.297388, 0.237910], 'p_i': 10, 'u_i': 2.6411},
        {'id': 1, 'e_m': 1.195922, 'e_o_k': [0.332201, 0.265760], 'p_i': 20, 'u_i': 4.9928},
        {'id': 2, 'e_m': 3.179254, 'e_o_k': [0.883126, 0.706501], 'p_i': 40, 'u_i': 3.9733},
        {'id': 3, 'e_m': 2.010249, 'e_o_k': [0.558403, 0.446722], 'p_i': 80, 'u_i': 1.2745},
        {'id': 4, 'e_m': 0.294507, 'e_o_k': [0.081808, 0.065446], 'p_i': 10, 'u_i': 1.8926},
        {'id': 5, 'e_m': 1.250085, 'e_o_k': [0.347246, 0.277797], 'p_i': 40, 'u_i': 4.4301},
        {'id': 6, 'e_m': 2.310377, 'e_o_k': [0.641771, 0.513417], 'p_i': 40, 'u_i': 2.8023},
        {'id': 7, 'e_m': 0.100727, 'e_o_k': [0.027980, 0.022384], 'p_i': 10, 'u_i': 1.0101},
    ]
    B_BUDGET = 55.200016
    return processors, tasks, B_BUDGET
