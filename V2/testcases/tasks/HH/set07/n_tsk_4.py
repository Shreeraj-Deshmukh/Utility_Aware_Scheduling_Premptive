"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.404244, 'e_o_k': [0.191715, 0.153372, 0.122697, 0.098158], 'p_i': 10, 'u_i': 3.9662},
        {'id': 1, 'e_m': 1.599701, 'e_o_k': [0.917861, 0.734289, 0.587431], 'p_i': 20, 'u_i': 1.8989},
        {'id': 2, 'e_m': 11.040808, 'e_o_k': [8.587295, 6.869836], 'p_i': 40, 'u_i': 3.5356},
        {'id': 3, 'e_m': 32.285624, 'e_o_k': [12.251679, 9.801343, 7.841074, 6.272860, 5.018288, 4.014630], 'p_i': 80, 'u_i': 1.2138},
    ]
    B_BUDGET = 176.639991
    return processors, tasks, B_BUDGET
