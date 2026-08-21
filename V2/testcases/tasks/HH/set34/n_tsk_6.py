"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.305521, 'e_o_k': [0.175299, 0.140239, 0.112191], 'p_i': 10, 'u_i': 2.4499},
        {'id': 1, 'e_m': 1.667370, 'e_o_k': [1.296843, 1.037475], 'p_i': 20, 'u_i': 1.6318},
        {'id': 2, 'e_m': 15.422385, 'e_o_k': [7.314139, 5.851311, 4.681049, 3.744839], 'p_i': 40, 'u_i': 3.2685},
        {'id': 3, 'e_m': 9.092490, 'e_o_k': [5.217003, 4.173602, 3.338882], 'p_i': 80, 'u_i': 2.9234},
        {'id': 4, 'e_m': 11.462298, 'e_o_k': [6.576728, 5.261383, 4.209106], 'p_i': 80, 'u_i': 3.7707},
        {'id': 5, 'e_m': 0.871698, 'e_o_k': [0.500155, 0.400124, 0.320099], 'p_i': 20, 'u_i': 1.9627},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET
