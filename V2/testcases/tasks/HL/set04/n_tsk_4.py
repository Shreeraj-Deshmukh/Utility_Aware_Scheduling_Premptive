"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.003558, 'e_o_k': [0.271538, 0.217230, 0.173784, 0.139027, 0.111222, 0.088978], 'p_i': 10, 'u_i': 3.5500},
        {'id': 1, 'e_m': 0.144137, 'e_o_k': [0.029536, 0.023629, 0.018903], 'p_i': 20, 'u_i': 2.3662},
        {'id': 2, 'e_m': 9.164294, 'e_o_k': [2.545637, 2.036510], 'p_i': 40, 'u_i': 3.8013},
        {'id': 3, 'e_m': 29.066399, 'e_o_k': [5.956229, 4.764983, 3.811987], 'p_i': 80, 'u_i': 4.3808},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET
