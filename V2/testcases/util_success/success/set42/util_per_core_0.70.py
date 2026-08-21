"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440003, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440003, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.389544, 'e_o_k': [0.112993, 0.090394, 0.072316, 0.057852, 0.046282, 0.037026], 'p_i': 10, 'u_i': 1.8568},
        {'id': 1, 'e_m': 6.423625, 'e_o_k': [0.789790, 0.631832, 0.505466], 'p_i': 20, 'u_i': 1.8128},
        {'id': 2, 'e_m': 3.359714, 'e_o_k': [0.559952, 0.447962], 'p_i': 40, 'u_i': 1.5689},
        {'id': 3, 'e_m': 5.016403, 'e_o_k': [0.509797, 0.407838, 0.326270, 0.261016], 'p_i': 80, 'u_i': 4.8976},
        {'id': 4, 'e_m': 1.333197, 'e_o_k': [0.108411, 0.086729, 0.069383, 0.055507, 0.044405, 0.035524], 'p_i': 40, 'u_i': 2.5447},
        {'id': 5, 'e_m': 14.292446, 'e_o_k': [2.382074, 1.905659], 'p_i': 40, 'u_i': 1.6969},
        {'id': 6, 'e_m': 4.067652, 'e_o_k': [0.413379, 0.330703, 0.264563, 0.211650], 'p_i': 80, 'u_i': 4.6966},
        {'id': 7, 'e_m': 28.134383, 'e_o_k': [2.510803, 2.008642, 1.606914, 1.285531, 1.028425], 'p_i': 80, 'u_i': 4.2096},
    ]
    B_BUDGET = 167.440003
    return processors, tasks, B_BUDGET
