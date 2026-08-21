"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.165491, 'e_o_k': [0.601525, 0.481220], 'p_i': 10, 'u_i': 4.6007},
        {'id': 1, 'e_m': 0.088973, 'e_o_k': [0.013234, 0.010587, 0.008470, 0.006776, 0.005421], 'p_i': 20, 'u_i': 4.4928},
        {'id': 2, 'e_m': 1.326107, 'e_o_k': [0.179724, 0.143780, 0.115024, 0.092019, 0.073615, 0.058892], 'p_i': 40, 'u_i': 4.0915},
        {'id': 3, 'e_m': 0.609452, 'e_o_k': [0.082598, 0.066078, 0.052863, 0.042290, 0.033832, 0.027066], 'p_i': 80, 'u_i': 4.3648},
        {'id': 4, 'e_m': 1.901509, 'e_o_k': [0.528197, 0.422558], 'p_i': 80, 'u_i': 3.7706},
        {'id': 5, 'e_m': 2.289249, 'e_o_k': [0.310257, 0.248206, 0.198564, 0.158852, 0.127081, 0.101665], 'p_i': 20, 'u_i': 4.9150},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET
