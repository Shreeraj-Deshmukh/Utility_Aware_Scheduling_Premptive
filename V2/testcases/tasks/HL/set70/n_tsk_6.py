"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.524362, 'e_o_k': [0.423434, 0.338747], 'p_i': 10, 'u_i': 1.8882},
        {'id': 1, 'e_m': 5.856002, 'e_o_k': [0.871014, 0.696811, 0.557449, 0.445959, 0.356767], 'p_i': 20, 'u_i': 2.0463},
        {'id': 2, 'e_m': 10.767148, 'e_o_k': [1.601492, 1.281193, 1.024955, 0.819964, 0.655971], 'p_i': 40, 'u_i': 1.5718},
        {'id': 3, 'e_m': 2.833997, 'e_o_k': [0.787221, 0.629777], 'p_i': 80, 'u_i': 2.9208},
        {'id': 4, 'e_m': 0.148278, 'e_o_k': [0.020096, 0.016077, 0.012861, 0.010289, 0.008231, 0.006585], 'p_i': 20, 'u_i': 4.6964},
        {'id': 5, 'e_m': 3.419689, 'e_o_k': [0.700756, 0.560605, 0.448484], 'p_i': 80, 'u_i': 4.6519},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
