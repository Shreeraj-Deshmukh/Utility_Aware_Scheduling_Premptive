"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.19999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.19999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471759, 'e_o_k': [0.079905, 0.063924, 0.051139, 0.040911], 'p_i': 10, 'u_i': 2.3827},
        {'id': 1, 'e_m': 1.719041, 'e_o_k': [0.255688, 0.204550, 0.163640, 0.130912, 0.104730], 'p_i': 20, 'u_i': 2.9856},
        {'id': 2, 'e_m': 0.035190, 'e_o_k': [0.004769, 0.003815, 0.003052, 0.002442, 0.001953, 0.001563], 'p_i': 40, 'u_i': 4.8236},
        {'id': 3, 'e_m': 8.778294, 'e_o_k': [1.486838, 1.189471, 0.951577, 0.761261], 'p_i': 80, 'u_i': 2.2531},
        {'id': 4, 'e_m': 11.210409, 'e_o_k': [1.667422, 1.333937, 1.067150, 0.853720, 0.682976], 'p_i': 80, 'u_i': 4.0598},
        {'id': 5, 'e_m': 0.322670, 'e_o_k': [0.054653, 0.043722, 0.034978, 0.027982], 'p_i': 20, 'u_i': 4.5014},
    ]
    B_BUDGET = 55.199990
    return processors, tasks, B_BUDGET
