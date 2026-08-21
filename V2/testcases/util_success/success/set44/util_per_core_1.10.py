"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120007, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120007, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.716707, 'e_o_k': [0.302230, 0.241784, 0.193427, 0.154742, 0.123794, 0.099035], 'p_i': 10, 'u_i': 3.6708},
        {'id': 1, 'e_m': 7.669091, 'e_o_k': [0.779379, 0.623503, 0.498803, 0.399042], 'p_i': 20, 'u_i': 1.7707},
        {'id': 2, 'e_m': 10.459638, 'e_o_k': [1.062971, 0.850377, 0.680302, 0.544241], 'p_i': 40, 'u_i': 4.2984},
        {'id': 3, 'e_m': 21.563052, 'e_o_k': [2.651195, 2.120956, 1.696765], 'p_i': 80, 'u_i': 4.5606},
        {'id': 4, 'e_m': 1.646195, 'e_o_k': [0.274366, 0.219493], 'p_i': 10, 'u_i': 3.0404},
        {'id': 5, 'e_m': 3.161745, 'e_o_k': [0.526957, 0.421566], 'p_i': 80, 'u_i': 1.9693},
        {'id': 6, 'e_m': 21.477797, 'e_o_k': [2.182703, 1.746162, 1.396930, 1.117544], 'p_i': 80, 'u_i': 3.7164},
        {'id': 7, 'e_m': 8.824639, 'e_o_k': [0.787539, 0.630031, 0.504025, 0.403220, 0.322576], 'p_i': 20, 'u_i': 2.2873},
    ]
    B_BUDGET = 263.120007
    return processors, tasks, B_BUDGET
