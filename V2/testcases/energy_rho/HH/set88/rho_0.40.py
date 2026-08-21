"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 114.815993, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.4, "seed": 1088, "set": 88, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 114.815993, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.4, "seed": 1088, "set": 88, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.686544, 'e_o_k': [0.393919, 0.315135, 0.252108], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 1.582739, 'e_o_k': [1.231019, 0.984815], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 5.107137, 'e_o_k': [2.422084, 1.937667, 1.550134, 1.240107], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.225789, 'e_o_k': [0.107082, 0.085665, 0.068532, 0.054826], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 10.028404, 'e_o_k': [4.176513, 3.341210, 2.672968, 2.138375, 1.710700], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 5.390837, 'e_o_k': [2.045703, 1.636563, 1.309250, 1.047400, 0.837920, 0.670336], 'p_i': 40, 'u_i': 4.5618},
        {'id': 6, 'e_m': 0.266387, 'e_o_k': [0.207190, 0.165752], 'p_i': 10, 'u_i': 3.9189},
        {'id': 7, 'e_m': 4.383523, 'e_o_k': [2.078907, 1.663125, 1.330500, 1.064400], 'p_i': 40, 'u_i': 2.1344},
    ]
    B_BUDGET = 114.815993
    return processors, tasks, B_BUDGET
