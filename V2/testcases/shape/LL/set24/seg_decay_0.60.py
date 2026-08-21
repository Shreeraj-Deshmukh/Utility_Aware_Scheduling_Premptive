"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127543, 'e_o_k': [0.027659, 0.016596, 0.009957, 0.005974, 0.003585], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 0.883465, 'e_o_k': [0.225374, 0.135224, 0.081135], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 2.358898, 'e_o_k': [0.511558, 0.306935, 0.184161, 0.110497, 0.066298], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 1.038301, 'e_o_k': [0.238580, 0.143148, 0.085889, 0.051533], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.490201, 'e_o_k': [0.102838, 0.061703, 0.037022, 0.022213, 0.013328, 0.007997], 'p_i': 40, 'u_i': 1.3531},
        {'id': 5, 'e_m': 14.146212, 'e_o_k': [4.420691, 2.652415], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.399627, 'e_o_k': [0.124883, 0.074930], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 0.841518, 'e_o_k': [0.193363, 0.116018, 0.069611, 0.041767], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
