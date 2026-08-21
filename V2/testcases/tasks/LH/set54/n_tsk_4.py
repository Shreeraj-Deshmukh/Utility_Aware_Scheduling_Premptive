"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.003191, 'e_o_k': [0.760166, 0.608133, 0.486507, 0.389205, 0.311364, 0.249091], 'p_i': 10, 'u_i': 3.2200},
        {'id': 1, 'e_m': 0.332245, 'e_o_k': [0.190632, 0.152506, 0.122005], 'p_i': 20, 'u_i': 1.6886},
        {'id': 2, 'e_m': 7.300599, 'e_o_k': [3.040468, 2.432375, 1.945900, 1.556720, 1.245376], 'p_i': 40, 'u_i': 4.2653},
        {'id': 3, 'e_m': 0.044298, 'e_o_k': [0.016810, 0.013448, 0.010759, 0.008607, 0.006885, 0.005508], 'p_i': 80, 'u_i': 3.8195},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
