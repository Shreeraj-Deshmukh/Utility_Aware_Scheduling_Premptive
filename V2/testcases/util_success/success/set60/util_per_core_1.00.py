"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.2, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.2, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.179057, 'e_o_k': [0.029843, 0.023874], 'p_i': 10, 'u_i': 4.4097},
        {'id': 1, 'e_m': 4.756852, 'e_o_k': [0.424517, 0.339613, 0.271691, 0.217353, 0.173882], 'p_i': 20, 'u_i': 3.2552},
        {'id': 2, 'e_m': 2.521797, 'e_o_k': [0.310057, 0.248046, 0.198437], 'p_i': 40, 'u_i': 4.2495},
        {'id': 3, 'e_m': 29.763096, 'e_o_k': [3.659397, 2.927518, 2.342014], 'p_i': 80, 'u_i': 2.9729},
        {'id': 4, 'e_m': 11.825933, 'e_o_k': [1.055384, 0.844307, 0.675446, 0.540357, 0.432285], 'p_i': 40, 'u_i': 2.0084},
        {'id': 5, 'e_m': 7.587790, 'e_o_k': [0.617014, 0.493611, 0.394889, 0.315911, 0.252729, 0.202183], 'p_i': 80, 'u_i': 3.7991},
        {'id': 6, 'e_m': 18.217467, 'e_o_k': [3.036244, 2.428996], 'p_i': 40, 'u_i': 1.2296},
        {'id': 7, 'e_m': 9.264714, 'e_o_k': [0.941536, 0.753229, 0.602583, 0.482066], 'p_i': 20, 'u_i': 3.7863},
    ]
    B_BUDGET = 239.200000
    return processors, tasks, B_BUDGET
