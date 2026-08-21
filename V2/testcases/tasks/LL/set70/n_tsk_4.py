"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.187791, 'e_o_k': [0.201184, 0.160947, 0.128758, 0.103006], 'p_i': 10, 'u_i': 4.7862},
        {'id': 1, 'e_m': 3.936347, 'e_o_k': [0.806628, 0.645303, 0.516242], 'p_i': 20, 'u_i': 1.7928},
        {'id': 2, 'e_m': 3.328741, 'e_o_k': [0.924650, 0.739720], 'p_i': 40, 'u_i': 1.8882},
        {'id': 3, 'e_m': 0.094804, 'e_o_k': [0.014101, 0.011281, 0.009025, 0.007220, 0.005776], 'p_i': 80, 'u_i': 2.0463},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET
