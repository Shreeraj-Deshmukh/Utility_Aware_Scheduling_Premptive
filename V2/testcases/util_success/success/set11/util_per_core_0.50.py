"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599994, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599994, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.334452, 'e_o_k': [0.119091, 0.095273, 0.076218, 0.060974, 0.048780], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 7.629503, 'e_o_k': [1.271584, 1.017267], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 5.672194, 'e_o_k': [0.945366, 0.756293], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 5.068683, 'e_o_k': [0.412168, 0.329735, 0.263788, 0.211030, 0.168824, 0.135059], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.436473, 'e_o_k': [0.072745, 0.058196], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.863739, 'e_o_k': [0.106197, 0.084958, 0.067966], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 6.795737, 'e_o_k': [0.690624, 0.552499, 0.441999, 0.353599], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 3.470880, 'e_o_k': [0.426748, 0.341398, 0.273118], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 119.599994
    return processors, tasks, B_BUDGET
