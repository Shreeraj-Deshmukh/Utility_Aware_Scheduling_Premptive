"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.323008, 'e_o_k': [0.562840, 0.450272, 0.360218, 0.288174], 'p_i': 10, 'u_i': 4.1671},
        {'id': 1, 'e_m': 0.682930, 'e_o_k': [0.139945, 0.111956, 0.089565], 'p_i': 20, 'u_i': 4.3098},
        {'id': 2, 'e_m': 3.722341, 'e_o_k': [0.630478, 0.504382, 0.403506, 0.322805], 'p_i': 40, 'u_i': 1.7953},
        {'id': 3, 'e_m': 27.239535, 'e_o_k': [3.691714, 2.953371, 2.362697, 1.890158, 1.512126, 1.209701], 'p_i': 80, 'u_i': 2.0773},
    ]
    B_BUDGET = 110.400007
    return processors, tasks, B_BUDGET
