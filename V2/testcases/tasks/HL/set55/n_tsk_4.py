"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.464668, 'e_o_k': [0.914891, 0.731913, 0.585530], 'p_i': 10, 'u_i': 2.7485},
        {'id': 1, 'e_m': 2.898867, 'e_o_k': [0.431174, 0.344939, 0.275951, 0.220761, 0.176609], 'p_i': 20, 'u_i': 3.8876},
        {'id': 2, 'e_m': 3.597911, 'e_o_k': [0.535149, 0.428119, 0.342495, 0.273996, 0.219197], 'p_i': 40, 'u_i': 1.4132},
        {'id': 3, 'e_m': 9.491363, 'e_o_k': [1.607616, 1.286093, 1.028874, 0.823099], 'p_i': 80, 'u_i': 3.6535},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET
