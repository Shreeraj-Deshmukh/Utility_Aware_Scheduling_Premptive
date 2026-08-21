"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599997, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599997, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.318857, 'e_o_k': [0.028456, 0.022765, 0.018212, 0.014569, 0.011656], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 2.208662, 'e_o_k': [0.271557, 0.217245, 0.173796], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 5.897245, 'e_o_k': [0.526289, 0.421031, 0.336825, 0.269460, 0.215568], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 2.595753, 'e_o_k': [0.263796, 0.211037, 0.168829, 0.135064], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 1.225501, 'e_o_k': [0.099654, 0.079723, 0.063778, 0.051023, 0.040818, 0.032655], 'p_i': 40, 'u_i': 1.3531},
        {'id': 5, 'e_m': 35.365531, 'e_o_k': [5.894255, 4.715404], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.999067, 'e_o_k': [0.166511, 0.133209], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 2.103795, 'e_o_k': [0.213800, 0.171040, 0.136832, 0.109466], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 119.599997
    return processors, tasks, B_BUDGET
