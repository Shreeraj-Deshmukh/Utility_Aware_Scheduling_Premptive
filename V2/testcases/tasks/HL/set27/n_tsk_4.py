"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.281059, 'e_o_k': [0.078072, 0.062458], 'p_i': 10, 'u_i': 4.6007},
        {'id': 1, 'e_m': 1.389833, 'e_o_k': [0.206722, 0.165378, 0.132302, 0.105842, 0.084673], 'p_i': 20, 'u_i': 4.4928},
        {'id': 2, 'e_m': 14.287523, 'e_o_k': [1.936357, 1.549085, 1.239268, 0.991415, 0.793132, 0.634505], 'p_i': 40, 'u_i': 4.0915},
        {'id': 3, 'e_m': 27.617149, 'e_o_k': [3.742891, 2.994313, 2.395451, 1.916360, 1.533088, 1.226471], 'p_i': 80, 'u_i': 4.3648},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
