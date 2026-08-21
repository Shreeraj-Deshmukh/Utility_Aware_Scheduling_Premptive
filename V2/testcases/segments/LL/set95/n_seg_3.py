"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.791911, 'e_o_k': [0.162277, 0.129821, 0.103857], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 1.455094, 'e_o_k': [0.298175, 0.238540, 0.190832], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 3.411616, 'e_o_k': [0.699102, 0.559281, 0.447425], 'p_i': 40, 'u_i': 4.3076},
        {'id': 3, 'e_m': 1.509835, 'e_o_k': [0.309393, 0.247514, 0.198011], 'p_i': 80, 'u_i': 2.0651},
        {'id': 4, 'e_m': 1.958205, 'e_o_k': [0.401272, 0.321017, 0.256814], 'p_i': 80, 'u_i': 2.7475},
        {'id': 5, 'e_m': 1.353233, 'e_o_k': [0.277302, 0.221841, 0.177473], 'p_i': 40, 'u_i': 2.9584},
        {'id': 6, 'e_m': 4.115647, 'e_o_k': [0.843370, 0.674696, 0.539757], 'p_i': 80, 'u_i': 3.8181},
        {'id': 7, 'e_m': 0.682738, 'e_o_k': [0.139905, 0.111924, 0.089539], 'p_i': 20, 'u_i': 3.4213},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
