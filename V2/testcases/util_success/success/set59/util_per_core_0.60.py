"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520006, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520006, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.380521, 'e_o_k': [0.356209, 0.284968, 0.227974, 0.182379, 0.145903, 0.116723], 'p_i': 10, 'u_i': 3.0949},
        {'id': 1, 'e_m': 1.251621, 'e_o_k': [0.153888, 0.123110, 0.098488], 'p_i': 20, 'u_i': 1.9752},
        {'id': 2, 'e_m': 6.952159, 'e_o_k': [0.620433, 0.496346, 0.397077, 0.317662, 0.254129], 'p_i': 40, 'u_i': 3.9662},
        {'id': 3, 'e_m': 0.951913, 'e_o_k': [0.117038, 0.093631, 0.074905], 'p_i': 80, 'u_i': 1.9890},
        {'id': 4, 'e_m': 5.185778, 'e_o_k': [0.462796, 0.370236, 0.296189, 0.236951, 0.189561], 'p_i': 40, 'u_i': 3.3639},
        {'id': 5, 'e_m': 0.631663, 'e_o_k': [0.064193, 0.051355, 0.041084, 0.032867], 'p_i': 10, 'u_i': 4.7869},
        {'id': 6, 'e_m': 0.621012, 'e_o_k': [0.063111, 0.050489, 0.040391, 0.032313], 'p_i': 10, 'u_i': 2.7944},
        {'id': 7, 'e_m': 2.587521, 'e_o_k': [0.431253, 0.345003], 'p_i': 10, 'u_i': 4.7769},
    ]
    B_BUDGET = 143.520006
    return processors, tasks, B_BUDGET
