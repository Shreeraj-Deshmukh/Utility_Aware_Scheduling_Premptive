"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119987, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119987, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.638188, 'e_o_k': [0.166482, 0.133186, 0.106549, 0.085239], 'p_i': 10, 'u_i': 3.7998},
        {'id': 1, 'e_m': 6.350399, 'e_o_k': [0.645366, 0.516293, 0.413034, 0.330427], 'p_i': 20, 'u_i': 4.4571},
        {'id': 2, 'e_m': 11.631964, 'e_o_k': [1.182110, 0.945688, 0.756550, 0.605240], 'p_i': 40, 'u_i': 3.7035},
        {'id': 3, 'e_m': 1.755852, 'e_o_k': [0.178440, 0.142752, 0.114202, 0.091361], 'p_i': 80, 'u_i': 3.6630},
        {'id': 4, 'e_m': 2.688167, 'e_o_k': [0.273188, 0.218550, 0.174840, 0.139872], 'p_i': 10, 'u_i': 4.5064},
        {'id': 5, 'e_m': 3.640817, 'e_o_k': [0.296059, 0.236847, 0.189478, 0.151582, 0.121266, 0.097013], 'p_i': 20, 'u_i': 1.1793},
        {'id': 6, 'e_m': 9.833256, 'e_o_k': [1.209007, 0.967205, 0.773764], 'p_i': 20, 'u_i': 2.9376},
        {'id': 7, 'e_m': 18.535745, 'e_o_k': [3.089291, 2.471433], 'p_i': 40, 'u_i': 3.3258},
    ]
    B_BUDGET = 263.119987
    return processors, tasks, B_BUDGET
