"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127543, 'e_o_k': [0.035429, 0.028343], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 0.883465, 'e_o_k': [0.245407, 0.196326], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 2.358898, 'e_o_k': [0.655249, 0.524200], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 1.038301, 'e_o_k': [0.288417, 0.230734], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.490201, 'e_o_k': [0.136167, 0.108933], 'p_i': 40, 'u_i': 1.1407},
        {'id': 5, 'e_m': 14.146212, 'e_o_k': [3.929503, 3.143603], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.399627, 'e_o_k': [0.111007, 0.088806], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 0.841518, 'e_o_k': [0.233755, 0.187004], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
