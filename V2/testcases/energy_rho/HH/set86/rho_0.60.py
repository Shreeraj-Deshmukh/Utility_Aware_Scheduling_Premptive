"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 135.423991, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.6, "seed": 1086, "set": 86, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 135.423991, "H": 80, "J": 23, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.6, "seed": 1086, "set": 86, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.100443, 'e_o_k': [0.057631, 0.046105, 0.036884], 'p_i': 10, 'u_i': 2.4144},
        {'id': 1, 'e_m': 0.413851, 'e_o_k': [0.321884, 0.257507], 'p_i': 20, 'u_i': 2.6559},
        {'id': 2, 'e_m': 2.380758, 'e_o_k': [0.991511, 0.793208, 0.634567, 0.507653, 0.406123], 'p_i': 40, 'u_i': 2.8681},
        {'id': 3, 'e_m': 13.943895, 'e_o_k': [10.845252, 8.676202], 'p_i': 80, 'u_i': 1.8896},
        {'id': 4, 'e_m': 1.101724, 'e_o_k': [0.458833, 0.367067, 0.293653, 0.234923, 0.187938], 'p_i': 20, 'u_i': 1.6645},
        {'id': 5, 'e_m': 0.583734, 'e_o_k': [0.243107, 0.194485, 0.155588, 0.124471, 0.099576], 'p_i': 40, 'u_i': 1.3774},
        {'id': 6, 'e_m': 3.223359, 'e_o_k': [2.507057, 2.005645], 'p_i': 80, 'u_i': 1.9412},
        {'id': 7, 'e_m': 34.037914, 'e_o_k': [26.473933, 21.179146], 'p_i': 80, 'u_i': 2.2237},
    ]
    B_BUDGET = 135.423991
    return processors, tasks, B_BUDGET
