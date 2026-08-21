"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.014200, 'e_o_k': [0.281722, 0.225378], 'p_i': 10, 'u_i': 1.1535},
        {'id': 1, 'e_m': 0.866375, 'e_o_k': [0.146744, 0.117395, 0.093916, 0.075133], 'p_i': 20, 'u_i': 2.8332},
        {'id': 2, 'e_m': 1.359317, 'e_o_k': [0.377588, 0.302070], 'p_i': 40, 'u_i': 2.4233},
        {'id': 3, 'e_m': 17.702265, 'e_o_k': [2.399149, 1.919319, 1.535455, 1.228364, 0.982691, 0.786153], 'p_i': 80, 'u_i': 4.2523},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
