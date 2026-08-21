"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.415096, 'e_o_k': [0.210479, 0.168384, 0.134707, 0.107765, 0.086212], 'p_i': 10, 'u_i': 3.0842},
        {'id': 1, 'e_m': 0.907251, 'e_o_k': [0.153667, 0.122934, 0.098347, 0.078678], 'p_i': 20, 'u_i': 4.6180},
        {'id': 2, 'e_m': 2.215453, 'e_o_k': [0.329524, 0.263619, 0.210895, 0.168716, 0.134973], 'p_i': 40, 'u_i': 1.1953},
        {'id': 3, 'e_m': 7.270569, 'e_o_k': [1.489871, 1.191897, 0.953517], 'p_i': 80, 'u_i': 1.1811},
        {'id': 4, 'e_m': 0.587338, 'e_o_k': [0.087360, 0.069888, 0.055910, 0.044728, 0.035783], 'p_i': 40, 'u_i': 1.7367},
        {'id': 5, 'e_m': 2.087040, 'e_o_k': [0.282852, 0.226282, 0.181025, 0.144820, 0.115856, 0.092685], 'p_i': 40, 'u_i': 3.6203},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
