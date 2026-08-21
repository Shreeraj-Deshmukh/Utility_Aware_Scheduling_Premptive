"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279989, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279989, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.491953, 'e_o_k': [0.081992, 0.065594], 'p_i': 10, 'u_i': 3.6093},
        {'id': 1, 'e_m': 4.055647, 'e_o_k': [0.675941, 0.540753], 'p_i': 20, 'u_i': 4.7651},
        {'id': 2, 'e_m': 10.618324, 'e_o_k': [1.305532, 1.044425, 0.835540], 'p_i': 40, 'u_i': 1.8328},
        {'id': 3, 'e_m': 10.598258, 'e_o_k': [0.861815, 0.689452, 0.551562, 0.441249, 0.352999, 0.282400], 'p_i': 80, 'u_i': 3.3737},
        {'id': 4, 'e_m': 1.859901, 'e_o_k': [0.151241, 0.120993, 0.096794, 0.077435, 0.061948, 0.049559], 'p_i': 10, 'u_i': 3.9221},
        {'id': 5, 'e_m': 9.764517, 'e_o_k': [0.871417, 0.697133, 0.557707, 0.446165, 0.356932], 'p_i': 20, 'u_i': 4.2804},
        {'id': 6, 'e_m': 2.198592, 'e_o_k': [0.178782, 0.143026, 0.114421, 0.091536, 0.073229, 0.058583], 'p_i': 10, 'u_i': 4.8852},
        {'id': 7, 'e_m': 20.480871, 'e_o_k': [3.413479, 2.730783], 'p_i': 80, 'u_i': 3.2811},
    ]
    B_BUDGET = 215.279989
    return processors, tasks, B_BUDGET
