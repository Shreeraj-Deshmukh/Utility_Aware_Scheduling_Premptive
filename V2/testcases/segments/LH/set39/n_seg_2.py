"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.217662, 'e_o_k': [0.169293, 0.135434], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 1.846208, 'e_o_k': [1.435940, 1.148752], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 0.830898, 'e_o_k': [0.646254, 0.517003], 'p_i': 40, 'u_i': 4.0270},
        {'id': 3, 'e_m': 10.940022, 'e_o_k': [8.508906, 6.807125], 'p_i': 80, 'u_i': 3.7051},
        {'id': 4, 'e_m': 0.087893, 'e_o_k': [0.068361, 0.054689], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.266000, 'e_o_k': [0.206889, 0.165511], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.085726, 'e_o_k': [0.066676, 0.053340], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 2.042668, 'e_o_k': [1.588742, 1.270993], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET
