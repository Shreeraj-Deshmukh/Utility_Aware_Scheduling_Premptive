"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640015, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640015, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.141191, 'e_o_k': [1.665371, 1.332296], 'p_i': 10, 'u_i': 2.6411},
        {'id': 1, 'e_m': 2.391844, 'e_o_k': [1.860323, 1.488259], 'p_i': 20, 'u_i': 4.9928},
        {'id': 2, 'e_m': 6.358508, 'e_o_k': [4.945506, 3.956405], 'p_i': 40, 'u_i': 3.9733},
        {'id': 3, 'e_m': 4.020499, 'e_o_k': [3.127054, 2.501644], 'p_i': 80, 'u_i': 1.2745},
        {'id': 4, 'e_m': 0.589014, 'e_o_k': [0.458122, 0.366498], 'p_i': 10, 'u_i': 1.8926},
        {'id': 5, 'e_m': 2.500170, 'e_o_k': [1.944576, 1.555661], 'p_i': 40, 'u_i': 4.4301},
        {'id': 6, 'e_m': 4.620754, 'e_o_k': [3.593920, 2.875136], 'p_i': 40, 'u_i': 2.8023},
        {'id': 7, 'e_m': 0.201453, 'e_o_k': [0.156686, 0.125349], 'p_i': 10, 'u_i': 1.0101},
    ]
    B_BUDGET = 176.640015
    return processors, tasks, B_BUDGET
