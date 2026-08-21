"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 22, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 22, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.028851, 'e_o_k': [0.007360, 0.004416, 0.002650], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 0.425044, 'e_o_k': [0.132826, 0.079696], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.371477, 'e_o_k': [0.080560, 0.048336, 0.029001, 0.017401, 0.010441], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 3.599048, 'e_o_k': [0.918124, 0.550875, 0.330525], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 5.420557, 'e_o_k': [1.175520, 0.705312, 0.423187, 0.253912, 0.152347], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 15.171358, 'e_o_k': [3.870244, 2.322147, 1.393288], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 0.633743, 'e_o_k': [0.145621, 0.087373, 0.052424, 0.031454], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 2.600128, 'e_o_k': [0.812540, 0.487524], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET
