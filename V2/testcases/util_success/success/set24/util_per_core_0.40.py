"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255086, 'e_o_k': [0.022765, 0.018212, 0.014569, 0.011656, 0.009324], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 1.766930, 'e_o_k': [0.217245, 0.173796, 0.139037], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 4.717796, 'e_o_k': [0.421031, 0.336825, 0.269460, 0.215568, 0.172454], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 2.076602, 'e_o_k': [0.211037, 0.168829, 0.135064, 0.108051], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.980401, 'e_o_k': [0.079723, 0.063778, 0.051023, 0.040818, 0.032655, 0.026124], 'p_i': 40, 'u_i': 1.3531},
        {'id': 5, 'e_m': 28.292425, 'e_o_k': [4.715404, 3.772323], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.799254, 'e_o_k': [0.133209, 0.106567], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 1.683036, 'e_o_k': [0.171040, 0.136832, 0.109466, 0.087573], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 95.680003
    return processors, tasks, B_BUDGET
