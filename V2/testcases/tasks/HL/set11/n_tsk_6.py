"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.453571, 'e_o_k': [0.297863, 0.238290, 0.190632], 'p_i': 10, 'u_i': 1.4749},
        {'id': 1, 'e_m': 7.609330, 'e_o_k': [1.288843, 1.031075, 0.824860, 0.659888], 'p_i': 20, 'u_i': 4.2682},
        {'id': 2, 'e_m': 4.803876, 'e_o_k': [0.714522, 0.571618, 0.457294, 0.365835, 0.292668], 'p_i': 40, 'u_i': 4.6830},
        {'id': 3, 'e_m': 4.130258, 'e_o_k': [1.147294, 0.917835], 'p_i': 80, 'u_i': 2.4027},
        {'id': 4, 'e_m': 1.771448, 'e_o_k': [0.492069, 0.393655], 'p_i': 80, 'u_i': 2.7203},
        {'id': 5, 'e_m': 3.212326, 'e_o_k': [0.435359, 0.348288, 0.278630, 0.222904, 0.178323, 0.142659], 'p_i': 40, 'u_i': 2.4000},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET
