"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.392989, 'e_o_k': [0.225485, 0.180388, 0.144311], 'p_i': 10, 'u_i': 3.6850},
        {'id': 1, 'e_m': 1.450345, 'e_o_k': [0.687833, 0.550266, 0.440213, 0.352171], 'p_i': 20, 'u_i': 3.7169},
        {'id': 2, 'e_m': 14.787038, 'e_o_k': [8.484366, 6.787493, 5.429994], 'p_i': 40, 'u_i': 3.7239},
        {'id': 3, 'e_m': 10.342252, 'e_o_k': [4.904862, 3.923890, 3.139112, 2.511289], 'p_i': 80, 'u_i': 1.9107},
        {'id': 4, 'e_m': 8.055015, 'e_o_k': [3.354659, 2.683727, 2.146982, 1.717585, 1.374068], 'p_i': 80, 'u_i': 1.7322},
        {'id': 5, 'e_m': 1.770841, 'e_o_k': [0.737499, 0.589999, 0.472000, 0.377600, 0.302080], 'p_i': 20, 'u_i': 1.5709},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET
