"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.572605, 'e_o_k': [0.328544, 0.262835, 0.210268], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 0.565553, 'e_o_k': [0.324497, 0.259598, 0.207678], 'p_i': 20, 'u_i': 4.7220},
        {'id': 2, 'e_m': 0.817880, 'e_o_k': [0.469275, 0.375420, 0.300336], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 5.124820, 'e_o_k': [2.940470, 2.352376, 1.881901], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 2.116956, 'e_o_k': [1.214647, 0.971717, 0.777374], 'p_i': 20, 'u_i': 3.9894},
        {'id': 5, 'e_m': 0.218732, 'e_o_k': [0.125502, 0.100402, 0.080321], 'p_i': 10, 'u_i': 1.1602},
        {'id': 6, 'e_m': 1.046970, 'e_o_k': [0.600720, 0.480576, 0.384461], 'p_i': 20, 'u_i': 4.5224},
        {'id': 7, 'e_m': 3.990809, 'e_o_k': [2.289809, 1.831847, 1.465477], 'p_i': 80, 'u_i': 3.6370},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET
