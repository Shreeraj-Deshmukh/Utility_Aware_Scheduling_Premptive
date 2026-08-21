"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359989, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359989, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.462904, 'e_o_k': [0.548718, 0.438974, 0.351179], 'p_i': 10, 'u_i': 2.7743},
        {'id': 1, 'e_m': 6.154336, 'e_o_k': [0.625441, 0.500353, 0.400282, 0.320226], 'p_i': 20, 'u_i': 3.3191},
        {'id': 2, 'e_m': 13.472666, 'e_o_k': [1.656475, 1.325180, 1.060144], 'p_i': 40, 'u_i': 1.2504},
        {'id': 3, 'e_m': 32.628364, 'e_o_k': [2.653230, 2.122584, 1.698067, 1.358454, 1.086763, 0.869410], 'p_i': 80, 'u_i': 1.6478},
        {'id': 4, 'e_m': 0.247361, 'e_o_k': [0.022075, 0.017660, 0.014128, 0.011303, 0.009042], 'p_i': 10, 'u_i': 4.3413},
        {'id': 5, 'e_m': 0.507695, 'e_o_k': [0.062422, 0.049937, 0.039950], 'p_i': 20, 'u_i': 1.0636},
        {'id': 6, 'e_m': 0.782442, 'e_o_k': [0.069828, 0.055862, 0.044690, 0.035752, 0.028601], 'p_i': 20, 'u_i': 4.5969},
        {'id': 7, 'e_m': 0.241571, 'e_o_k': [0.029701, 0.023761, 0.019009], 'p_i': 20, 'u_i': 3.6081},
    ]
    B_BUDGET = 191.359989
    return processors, tasks, B_BUDGET
