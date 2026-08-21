"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759992, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759992, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.858908, 'e_o_k': [0.087287, 0.069830, 0.055864, 0.044691], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 0.848329, 'e_o_k': [0.068983, 0.055187, 0.044149, 0.035319, 0.028256, 0.022604], 'p_i': 20, 'u_i': 1.5082},
        {'id': 2, 'e_m': 1.226819, 'e_o_k': [0.124677, 0.099741, 0.079793, 0.063835], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 7.687229, 'e_o_k': [0.781222, 0.624978, 0.499982, 0.399986], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 3.175434, 'e_o_k': [0.258216, 0.206573, 0.165258, 0.132206, 0.105765, 0.084612], 'p_i': 20, 'u_i': 2.1026},
        {'id': 5, 'e_m': 0.328098, 'e_o_k': [0.026680, 0.021344, 0.017075, 0.013660, 0.010928, 0.008742], 'p_i': 10, 'u_i': 4.2691},
        {'id': 6, 'e_m': 1.570455, 'e_o_k': [0.127704, 0.102163, 0.081731, 0.065385, 0.052308, 0.041846], 'p_i': 20, 'u_i': 3.6679},
        {'id': 7, 'e_m': 5.986214, 'e_o_k': [0.997702, 0.798162], 'p_i': 80, 'u_i': 2.7165},
    ]
    B_BUDGET = 71.759992
    return processors, tasks, B_BUDGET
