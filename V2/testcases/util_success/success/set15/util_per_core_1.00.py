"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199993, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199993, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.122771, 'e_o_k': [0.091300, 0.073040, 0.058432, 0.046746, 0.037396, 0.029917], 'p_i': 10, 'u_i': 1.5997},
        {'id': 1, 'e_m': 3.177912, 'e_o_k': [0.529652, 0.423722], 'p_i': 20, 'u_i': 4.7941},
        {'id': 2, 'e_m': 13.818024, 'e_o_k': [1.404271, 1.123417, 0.898733, 0.718987], 'p_i': 40, 'u_i': 3.5328},
        {'id': 3, 'e_m': 20.587345, 'e_o_k': [1.674095, 1.339276, 1.071420, 0.857136, 0.685709, 0.548567], 'p_i': 80, 'u_i': 3.7747},
        {'id': 4, 'e_m': 9.503739, 'e_o_k': [0.848144, 0.678515, 0.542812, 0.434250, 0.347400], 'p_i': 40, 'u_i': 3.0844},
        {'id': 5, 'e_m': 16.789386, 'e_o_k': [1.365257, 1.092206, 0.873765, 0.699012, 0.559209, 0.447367], 'p_i': 40, 'u_i': 1.4908},
        {'id': 6, 'e_m': 32.703122, 'e_o_k': [5.450520, 4.360416], 'p_i': 80, 'u_i': 2.9455},
        {'id': 7, 'e_m': 0.599177, 'e_o_k': [0.099863, 0.079890], 'p_i': 10, 'u_i': 4.7629},
    ]
    B_BUDGET = 239.199993
    return processors, tasks, B_BUDGET
