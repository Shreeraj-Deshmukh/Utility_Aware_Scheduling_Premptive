"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.942324, 'e_o_k': [0.732919, 0.586335], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.718592, 'e_o_k': [0.558905, 0.447124], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.754744, 'e_o_k': [0.587023, 0.469618], 'p_i': 40, 'u_i': 4.4037},
        {'id': 3, 'e_m': 4.113295, 'e_o_k': [3.199230, 2.559384], 'p_i': 80, 'u_i': 1.7011},
        {'id': 4, 'e_m': 15.892935, 'e_o_k': [12.361171, 9.888937], 'p_i': 40, 'u_i': 1.8442},
        {'id': 5, 'e_m': 3.188381, 'e_o_k': [2.479852, 1.983882], 'p_i': 40, 'u_i': 2.3108},
        {'id': 6, 'e_m': 1.051973, 'e_o_k': [0.818201, 0.654561], 'p_i': 10, 'u_i': 1.0383},
        {'id': 7, 'e_m': 0.692921, 'e_o_k': [0.538938, 0.431151], 'p_i': 40, 'u_i': 2.0614},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
