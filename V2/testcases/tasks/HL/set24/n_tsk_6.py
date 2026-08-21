"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.354828, 'e_o_k': [0.048089, 0.038471, 0.030777, 0.024622, 0.019697, 0.015758], 'p_i': 10, 'u_i': 2.4636},
        {'id': 1, 'e_m': 2.540170, 'e_o_k': [0.430246, 0.344196, 0.275357, 0.220286], 'p_i': 20, 'u_i': 2.5536},
        {'id': 2, 'e_m': 6.878544, 'e_o_k': [1.910707, 1.528565], 'p_i': 40, 'u_i': 3.8458},
        {'id': 3, 'e_m': 3.325131, 'e_o_k': [0.681379, 0.545103, 0.436083], 'p_i': 80, 'u_i': 4.1906},
        {'id': 4, 'e_m': 0.549338, 'e_o_k': [0.152594, 0.122075], 'p_i': 10, 'u_i': 2.6385},
        {'id': 5, 'e_m': 29.523779, 'e_o_k': [4.391328, 3.513063, 2.810450, 2.248360, 1.798688], 'p_i': 80, 'u_i': 2.8958},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
