"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.20002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.177414, 'e_o_k': [0.024045, 0.019236, 0.015388, 0.012311, 0.009849, 0.007879], 'p_i': 10, 'u_i': 2.4636},
        {'id': 1, 'e_m': 1.270085, 'e_o_k': [0.215123, 0.172098, 0.137679, 0.110143], 'p_i': 20, 'u_i': 2.5536},
        {'id': 2, 'e_m': 3.439272, 'e_o_k': [0.955353, 0.764283], 'p_i': 40, 'u_i': 3.8458},
        {'id': 3, 'e_m': 1.662565, 'e_o_k': [0.340690, 0.272552, 0.218041], 'p_i': 80, 'u_i': 4.1906},
        {'id': 4, 'e_m': 0.274669, 'e_o_k': [0.076297, 0.061038], 'p_i': 10, 'u_i': 2.6385},
        {'id': 5, 'e_m': 14.761889, 'e_o_k': [2.195664, 1.756531, 1.405225, 1.124180, 0.899344], 'p_i': 80, 'u_i': 2.8958},
    ]
    B_BUDGET = 55.200020
    return processors, tasks, B_BUDGET
