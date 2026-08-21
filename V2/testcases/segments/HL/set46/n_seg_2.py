"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.837512, 'e_o_k': [0.232642, 0.186114], 'p_i': 10, 'u_i': 3.9687},
        {'id': 1, 'e_m': 0.500247, 'e_o_k': [0.138957, 0.111166], 'p_i': 20, 'u_i': 3.3202},
        {'id': 2, 'e_m': 10.611361, 'e_o_k': [2.947600, 2.358080], 'p_i': 40, 'u_i': 4.3833},
        {'id': 3, 'e_m': 7.607968, 'e_o_k': [2.113324, 1.690659], 'p_i': 80, 'u_i': 1.8853},
        {'id': 4, 'e_m': 2.826180, 'e_o_k': [0.785050, 0.628040], 'p_i': 20, 'u_i': 2.6679},
        {'id': 5, 'e_m': 0.129053, 'e_o_k': [0.035848, 0.028679], 'p_i': 10, 'u_i': 2.8390},
        {'id': 6, 'e_m': 1.188189, 'e_o_k': [0.330052, 0.264042], 'p_i': 40, 'u_i': 3.5794},
        {'id': 7, 'e_m': 5.877351, 'e_o_k': [1.632598, 1.306078], 'p_i': 40, 'u_i': 4.0478},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
