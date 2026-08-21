"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.072889, 'e_o_k': [0.159580, 0.127664, 0.102131, 0.081705, 0.065364], 'p_i': 10, 'u_i': 4.5978},
        {'id': 1, 'e_m': 3.167930, 'e_o_k': [0.649166, 0.519333, 0.415466], 'p_i': 20, 'u_i': 3.9895},
        {'id': 2, 'e_m': 1.605579, 'e_o_k': [0.445994, 0.356795], 'p_i': 40, 'u_i': 3.6989},
        {'id': 3, 'e_m': 3.927160, 'e_o_k': [0.665169, 0.532135, 0.425708, 0.340567], 'p_i': 80, 'u_i': 3.2467},
        {'id': 4, 'e_m': 1.165551, 'e_o_k': [0.238842, 0.191074, 0.152859], 'p_i': 80, 'u_i': 4.5958},
        {'id': 5, 'e_m': 1.220649, 'e_o_k': [0.206749, 0.165400, 0.132320, 0.105856], 'p_i': 40, 'u_i': 4.0042},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
