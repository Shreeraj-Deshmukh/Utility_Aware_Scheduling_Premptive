"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.285319, 'e_o_k': [0.191177, 0.152941, 0.122353, 0.097882, 0.078306], 'p_i': 10, 'u_i': 2.3680},
        {'id': 1, 'e_m': 1.739923, 'e_o_k': [0.483312, 0.386650], 'p_i': 20, 'u_i': 4.2120},
        {'id': 2, 'e_m': 2.896760, 'e_o_k': [0.804656, 0.643724], 'p_i': 40, 'u_i': 4.4653},
        {'id': 3, 'e_m': 8.964238, 'e_o_k': [2.490066, 1.992053], 'p_i': 80, 'u_i': 4.6069},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
