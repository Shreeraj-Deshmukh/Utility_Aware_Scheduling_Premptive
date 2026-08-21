"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.141807, 'e_o_k': [0.154747, 0.123797, 0.099038, 0.079230, 0.063384, 0.050707], 'p_i': 10, 'u_i': 1.6837},
        {'id': 1, 'e_m': 2.144447, 'e_o_k': [0.595680, 0.476544], 'p_i': 20, 'u_i': 2.3942},
        {'id': 2, 'e_m': 4.652828, 'e_o_k': [0.692056, 0.553644, 0.442916, 0.354332, 0.283466], 'p_i': 40, 'u_i': 1.1399},
        {'id': 3, 'e_m': 4.982100, 'e_o_k': [0.675213, 0.540170, 0.432136, 0.345709, 0.276567, 0.221254], 'p_i': 80, 'u_i': 4.6324},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
