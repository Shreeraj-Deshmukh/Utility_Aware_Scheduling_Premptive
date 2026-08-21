"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.232409, 'e_o_k': [0.110221, 0.088177, 0.070541, 0.056433], 'p_i': 10, 'u_i': 4.2389},
        {'id': 1, 'e_m': 1.189114, 'e_o_k': [0.495228, 0.396183, 0.316946, 0.253557, 0.202845], 'p_i': 20, 'u_i': 4.7607},
        {'id': 2, 'e_m': 9.509979, 'e_o_k': [4.510153, 3.608122, 2.886498, 2.309198], 'p_i': 40, 'u_i': 3.2703},
        {'id': 3, 'e_m': 38.364318, 'e_o_k': [22.012313, 17.609851, 14.087881], 'p_i': 80, 'u_i': 4.5676},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
