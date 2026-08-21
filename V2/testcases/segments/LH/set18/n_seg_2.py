"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320009, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320009, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.498376, 'e_o_k': [0.387626, 0.310101], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 0.297010, 'e_o_k': [0.231008, 0.184806], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 0.891273, 'e_o_k': [0.693213, 0.554570], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 2.329510, 'e_o_k': [1.811841, 1.449473], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 0.437113, 'e_o_k': [0.339977, 0.271982], 'p_i': 20, 'u_i': 2.4561},
        {'id': 5, 'e_m': 9.162615, 'e_o_k': [7.126478, 5.701183], 'p_i': 80, 'u_i': 1.8035},
        {'id': 6, 'e_m': 0.776607, 'e_o_k': [0.604028, 0.483222], 'p_i': 20, 'u_i': 3.4846},
        {'id': 7, 'e_m': 1.086925, 'e_o_k': [0.845386, 0.676309], 'p_i': 10, 'u_i': 2.9402},
    ]
    B_BUDGET = 88.320009
    return processors, tasks, B_BUDGET
