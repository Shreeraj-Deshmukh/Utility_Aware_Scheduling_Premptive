"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.069906, 'e_o_k': [0.095482, 0.076385, 0.061108, 0.048887, 0.039109], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 2.577807, 'e_o_k': [0.209619, 0.167695, 0.134156, 0.107325, 0.085860, 0.068688], 'p_i': 20, 'u_i': 3.3367},
        {'id': 2, 'e_m': 2.245307, 'e_o_k': [0.276062, 0.220850, 0.176680], 'p_i': 40, 'u_i': 4.5472},
        {'id': 3, 'e_m': 0.911368, 'e_o_k': [0.092619, 0.074095, 0.059276, 0.047421], 'p_i': 80, 'u_i': 1.6834},
        {'id': 4, 'e_m': 2.777122, 'e_o_k': [0.462854, 0.370283], 'p_i': 40, 'u_i': 3.8684},
        {'id': 5, 'e_m': 17.407167, 'e_o_k': [2.901194, 2.320956], 'p_i': 40, 'u_i': 4.7513},
        {'id': 6, 'e_m': 7.438576, 'e_o_k': [0.604880, 0.483904, 0.387123, 0.309699, 0.247759, 0.198207], 'p_i': 40, 'u_i': 2.4512},
        {'id': 7, 'e_m': 0.060227, 'e_o_k': [0.010038, 0.008030], 'p_i': 10, 'u_i': 1.4858},
    ]
    B_BUDGET = 119.600001
    return processors, tasks, B_BUDGET
