"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.325064, 'e_o_k': [0.179583, 0.143666, 0.114933, 0.091947, 0.073557, 0.058846], 'p_i': 10, 'u_i': 3.4980},
        {'id': 1, 'e_m': 3.938877, 'e_o_k': [1.094133, 0.875306], 'p_i': 20, 'u_i': 2.1751},
        {'id': 2, 'e_m': 1.537214, 'e_o_k': [0.228643, 0.182915, 0.146332, 0.117065, 0.093652], 'p_i': 40, 'u_i': 4.1688},
        {'id': 3, 'e_m': 5.703460, 'e_o_k': [1.168742, 0.934993, 0.747995], 'p_i': 80, 'u_i': 2.2140},
        {'id': 4, 'e_m': 1.856926, 'e_o_k': [0.380518, 0.304414, 0.243531], 'p_i': 10, 'u_i': 3.2266},
        {'id': 5, 'e_m': 1.751335, 'e_o_k': [0.237355, 0.189884, 0.151907, 0.121526, 0.097220, 0.077776], 'p_i': 10, 'u_i': 3.3398},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
