"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280009, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280009, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.390212, 'e_o_k': [0.031731, 0.025385, 0.020308, 0.016246, 0.012997, 0.010398], 'p_i': 10, 'u_i': 3.1766},
        {'id': 1, 'e_m': 7.337871, 'e_o_k': [0.596691, 0.477353, 0.381882, 0.305506, 0.244405, 0.195524], 'p_i': 20, 'u_i': 1.6887},
        {'id': 2, 'e_m': 2.062948, 'e_o_k': [0.184104, 0.147283, 0.117827, 0.094261, 0.075409], 'p_i': 40, 'u_i': 3.5480},
        {'id': 3, 'e_m': 26.497798, 'e_o_k': [2.692866, 2.154292, 1.723434, 1.378747], 'p_i': 80, 'u_i': 3.7765},
        {'id': 4, 'e_m': 11.998068, 'e_o_k': [1.070746, 0.856597, 0.685278, 0.548222, 0.438578], 'p_i': 40, 'u_i': 3.9794},
        {'id': 5, 'e_m': 12.576373, 'e_o_k': [1.546275, 1.237020, 0.989616], 'p_i': 80, 'u_i': 3.8371},
        {'id': 6, 'e_m': 3.375789, 'e_o_k': [0.562632, 0.450105], 'p_i': 10, 'u_i': 4.0284},
        {'id': 7, 'e_m': 17.324302, 'e_o_k': [1.408755, 1.127004, 0.901603, 0.721282, 0.577026, 0.461621], 'p_i': 80, 'u_i': 4.5608},
    ]
    B_BUDGET = 215.280009
    return processors, tasks, B_BUDGET
