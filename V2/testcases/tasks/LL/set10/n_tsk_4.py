"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.498114, 'e_o_k': [0.138365, 0.110692], 'p_i': 10, 'u_i': 2.6429},
        {'id': 1, 'e_m': 0.521769, 'e_o_k': [0.077607, 0.062086, 0.049669, 0.039735, 0.031788], 'p_i': 20, 'u_i': 1.6574},
        {'id': 2, 'e_m': 9.762141, 'e_o_k': [1.452008, 1.161606, 0.929285, 0.743428, 0.594742], 'p_i': 40, 'u_i': 4.4970},
        {'id': 3, 'e_m': 6.403733, 'e_o_k': [1.312240, 1.049792, 0.839834], 'p_i': 80, 'u_i': 1.4275},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET
