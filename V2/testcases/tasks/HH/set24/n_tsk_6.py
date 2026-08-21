"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.354828, 'e_o_k': [0.134649, 0.107719, 0.086176, 0.068940, 0.055152, 0.044122], 'p_i': 10, 'u_i': 2.4636},
        {'id': 1, 'e_m': 2.540170, 'e_o_k': [1.204688, 0.963750, 0.771000, 0.616800], 'p_i': 20, 'u_i': 2.5536},
        {'id': 2, 'e_m': 6.878544, 'e_o_k': [5.349979, 4.279983], 'p_i': 40, 'u_i': 3.8458},
        {'id': 3, 'e_m': 3.325131, 'e_o_k': [1.907862, 1.526289, 1.221032], 'p_i': 80, 'u_i': 4.1906},
        {'id': 4, 'e_m': 0.549338, 'e_o_k': [0.427263, 0.341810], 'p_i': 10, 'u_i': 2.6385},
        {'id': 5, 'e_m': 29.523779, 'e_o_k': [12.295719, 9.836575, 7.869260, 6.295408, 5.036327], 'p_i': 80, 'u_i': 2.8958},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
