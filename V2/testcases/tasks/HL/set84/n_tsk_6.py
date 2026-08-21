"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.670616, 'e_o_k': [0.090887, 0.072710, 0.058168, 0.046534, 0.037227, 0.029782], 'p_i': 10, 'u_i': 3.3883},
        {'id': 1, 'e_m': 1.064349, 'e_o_k': [0.158310, 0.126648, 0.101318, 0.081055, 0.064844], 'p_i': 20, 'u_i': 2.1673},
        {'id': 2, 'e_m': 6.847533, 'e_o_k': [0.928031, 0.742425, 0.593940, 0.475152, 0.380122, 0.304097], 'p_i': 40, 'u_i': 3.4649},
        {'id': 3, 'e_m': 4.269330, 'e_o_k': [0.723125, 0.578500, 0.462800, 0.370240], 'p_i': 80, 'u_i': 2.8434},
        {'id': 4, 'e_m': 0.700141, 'e_o_k': [0.143472, 0.114777, 0.091822], 'p_i': 20, 'u_i': 4.3788},
        {'id': 5, 'e_m': 4.201589, 'e_o_k': [0.711651, 0.569321, 0.455457, 0.364365], 'p_i': 10, 'u_i': 3.2500},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
