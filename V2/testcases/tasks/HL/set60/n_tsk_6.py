"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.962087, 'e_o_k': [0.545024, 0.436019], 'p_i': 10, 'u_i': 2.4321},
        {'id': 1, 'e_m': 7.737294, 'e_o_k': [1.048618, 0.838895, 0.671116, 0.536893, 0.429514, 0.343611], 'p_i': 20, 'u_i': 1.0700},
        {'id': 2, 'e_m': 1.138036, 'e_o_k': [0.233204, 0.186563, 0.149251], 'p_i': 40, 'u_i': 3.1686},
        {'id': 3, 'e_m': 9.481208, 'e_o_k': [1.942870, 1.554296, 1.243437], 'p_i': 80, 'u_i': 1.4833},
        {'id': 4, 'e_m': 0.197047, 'e_o_k': [0.026705, 0.021364, 0.017091, 0.013673, 0.010938, 0.008751], 'p_i': 20, 'u_i': 1.9048},
        {'id': 5, 'e_m': 2.404333, 'e_o_k': [0.667870, 0.534296], 'p_i': 40, 'u_i': 4.4078},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET
