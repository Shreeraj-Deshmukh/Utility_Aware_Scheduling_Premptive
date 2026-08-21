"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 23, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 23, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.791911, 'e_o_k': [0.134131, 0.107305, 0.085844, 0.068675], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 1.455094, 'e_o_k': [0.404193, 0.323354], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 3.411616, 'e_o_k': [0.462369, 0.369895, 0.295916, 0.236733, 0.189386, 0.151509], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 1.509835, 'e_o_k': [0.309393, 0.247514, 0.198011], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 1.958205, 'e_o_k': [0.265391, 0.212313, 0.169850, 0.135880, 0.108704, 0.086963], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 1.353233, 'e_o_k': [0.277302, 0.221841, 0.177473], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 4.115647, 'e_o_k': [0.612156, 0.489725, 0.391780, 0.313424, 0.250739], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 0.682738, 'e_o_k': [0.115640, 0.092512, 0.074010, 0.059208], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
