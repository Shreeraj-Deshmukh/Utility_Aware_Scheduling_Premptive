"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600006, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.687580, 'e_o_k': [0.218545, 0.174836, 0.139869, 0.111895, 0.089516, 0.071613], 'p_i': 10, 'u_i': 3.8590},
        {'id': 1, 'e_m': 0.346108, 'e_o_k': [0.030888, 0.024710, 0.019768, 0.015815, 0.012652], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 1.296129, 'e_o_k': [0.115671, 0.092537, 0.074029, 0.059223, 0.047379], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.327075, 'e_o_k': [0.054513, 0.043610], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 15.817945, 'e_o_k': [2.636324, 2.109059], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.210999, 'e_o_k': [0.035167, 0.028133], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 3.265633, 'e_o_k': [0.291436, 0.233148, 0.186519, 0.149215, 0.119372], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 4.178003, 'e_o_k': [0.513689, 0.410951, 0.328761], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 119.600006
    return processors, tasks, B_BUDGET
