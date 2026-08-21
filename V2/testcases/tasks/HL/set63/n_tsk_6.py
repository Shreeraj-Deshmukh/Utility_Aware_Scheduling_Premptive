"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399991, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399991, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.206954, 'e_o_k': [0.328259, 0.262608, 0.210086, 0.168069, 0.134455], 'p_i': 10, 'u_i': 2.2919},
        {'id': 1, 'e_m': 0.046886, 'e_o_k': [0.006354, 0.005083, 0.004067, 0.003253, 0.002603, 0.002082], 'p_i': 20, 'u_i': 3.9772},
        {'id': 2, 'e_m': 4.267678, 'e_o_k': [0.722845, 0.578276, 0.462621, 0.370097], 'p_i': 40, 'u_i': 1.4627},
        {'id': 3, 'e_m': 2.726716, 'e_o_k': [0.757421, 0.605937], 'p_i': 80, 'u_i': 4.5040},
        {'id': 4, 'e_m': 2.163074, 'e_o_k': [0.443253, 0.354602, 0.283682], 'p_i': 20, 'u_i': 4.7123},
        {'id': 5, 'e_m': 13.121227, 'e_o_k': [1.951634, 1.561307, 1.249046, 0.999237, 0.799389], 'p_i': 40, 'u_i': 4.3702},
    ]
    B_BUDGET = 110.399991
    return processors, tasks, B_BUDGET
