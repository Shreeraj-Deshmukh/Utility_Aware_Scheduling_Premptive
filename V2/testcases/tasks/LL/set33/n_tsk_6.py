"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.033694, 'e_o_k': [0.009359, 0.007488], 'p_i': 10, 'u_i': 2.5143},
        {'id': 1, 'e_m': 2.566344, 'e_o_k': [0.381715, 0.305372, 0.244297, 0.195438, 0.156350], 'p_i': 20, 'u_i': 1.6130},
        {'id': 2, 'e_m': 3.774422, 'e_o_k': [0.773447, 0.618758, 0.495006], 'p_i': 40, 'u_i': 1.3758},
        {'id': 3, 'e_m': 0.700248, 'e_o_k': [0.143493, 0.114795, 0.091836], 'p_i': 80, 'u_i': 3.6848},
        {'id': 4, 'e_m': 1.539074, 'e_o_k': [0.427521, 0.342016], 'p_i': 10, 'u_i': 1.6851},
        {'id': 5, 'e_m': 0.225847, 'e_o_k': [0.033592, 0.026874, 0.021499, 0.017199, 0.013759], 'p_i': 20, 'u_i': 1.3700},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET
