"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640015, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640015, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.970629, 'e_o_k': [0.556918, 0.445535, 0.356428], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 2.923011, 'e_o_k': [1.677137, 1.341710, 1.073368], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 1.109904, 'e_o_k': [0.636830, 0.509464, 0.407571], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 3.648613, 'e_o_k': [2.093466, 1.674773, 1.339818], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 1.035116, 'e_o_k': [0.593919, 0.475135, 0.380108], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 10.125219, 'e_o_k': [5.809552, 4.647641, 3.718113], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 4.891882, 'e_o_k': [2.806818, 2.245454, 1.796363], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.359380, 'e_o_k': [0.206202, 0.164962, 0.131969], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 176.640015
    return processors, tasks, B_BUDGET
