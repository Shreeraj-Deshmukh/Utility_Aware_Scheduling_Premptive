"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439997, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439997, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.847977, 'e_o_k': [0.104259, 0.083408, 0.066726], 'p_i': 10, 'u_i': 4.3788},
        {'id': 1, 'e_m': 1.676465, 'e_o_k': [0.170372, 0.136298, 0.109038, 0.087231], 'p_i': 20, 'u_i': 3.2500},
        {'id': 2, 'e_m': 4.827192, 'e_o_k': [0.804532, 0.643626], 'p_i': 40, 'u_i': 3.9101},
        {'id': 3, 'e_m': 4.327455, 'e_o_k': [0.439782, 0.351826, 0.281460, 0.225168], 'p_i': 80, 'u_i': 2.7187},
        {'id': 4, 'e_m': 10.166814, 'e_o_k': [0.826732, 0.661385, 0.529108, 0.423287, 0.338629, 0.270903], 'p_i': 80, 'u_i': 3.8755},
        {'id': 5, 'e_m': 17.095373, 'e_o_k': [2.101890, 1.681512, 1.345210], 'p_i': 40, 'u_i': 3.4836},
        {'id': 6, 'e_m': 19.823355, 'e_o_k': [2.437298, 1.949838, 1.559871], 'p_i': 80, 'u_i': 4.1699},
        {'id': 7, 'e_m': 5.086892, 'e_o_k': [0.516961, 0.413568, 0.330855, 0.264684], 'p_i': 20, 'u_i': 3.6851},
    ]
    B_BUDGET = 167.439997
    return processors, tasks, B_BUDGET
