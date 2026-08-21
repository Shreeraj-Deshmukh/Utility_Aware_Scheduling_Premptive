"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.837512, 'e_o_k': [0.171621, 0.137297, 0.109838], 'p_i': 10, 'u_i': 3.9687},
        {'id': 1, 'e_m': 0.500247, 'e_o_k': [0.102510, 0.082008, 0.065606], 'p_i': 20, 'u_i': 3.3202},
        {'id': 2, 'e_m': 10.611361, 'e_o_k': [2.174459, 1.739567, 1.391654], 'p_i': 40, 'u_i': 4.3833},
        {'id': 3, 'e_m': 7.607968, 'e_o_k': [1.559010, 1.247208, 0.997766], 'p_i': 80, 'u_i': 1.8853},
        {'id': 4, 'e_m': 2.826180, 'e_o_k': [0.579135, 0.463308, 0.370647], 'p_i': 20, 'u_i': 2.6679},
        {'id': 5, 'e_m': 0.129053, 'e_o_k': [0.026445, 0.021156, 0.016925], 'p_i': 10, 'u_i': 2.8390},
        {'id': 6, 'e_m': 1.188189, 'e_o_k': [0.243481, 0.194785, 0.155828], 'p_i': 40, 'u_i': 3.5794},
        {'id': 7, 'e_m': 5.877351, 'e_o_k': [1.204375, 0.963500, 0.770800], 'p_i': 40, 'u_i': 4.0478},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
