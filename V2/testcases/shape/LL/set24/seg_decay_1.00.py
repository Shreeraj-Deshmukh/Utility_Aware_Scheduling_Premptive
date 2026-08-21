"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127543, 'e_o_k': [0.012754, 0.012754, 0.012754, 0.012754, 0.012754], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 0.883465, 'e_o_k': [0.147244, 0.147244, 0.147244], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 2.358898, 'e_o_k': [0.235890, 0.235890, 0.235890, 0.235890, 0.235890], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 1.038301, 'e_o_k': [0.129788, 0.129788, 0.129788, 0.129788], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.490201, 'e_o_k': [0.040850, 0.040850, 0.040850, 0.040850, 0.040850, 0.040850], 'p_i': 40, 'u_i': 1.3531},
        {'id': 5, 'e_m': 14.146212, 'e_o_k': [3.536553, 3.536553], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.399627, 'e_o_k': [0.099907, 0.099907], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 0.841518, 'e_o_k': [0.105190, 0.105190, 0.105190, 0.105190], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
