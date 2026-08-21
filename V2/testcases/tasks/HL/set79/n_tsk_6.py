"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399986, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399986, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.935752, 'e_o_k': [0.126820, 0.101456, 0.081165, 0.064932, 0.051946, 0.041557], 'p_i': 10, 'u_i': 2.7067},
        {'id': 1, 'e_m': 2.374259, 'e_o_k': [0.321778, 0.257422, 0.205938, 0.164750, 0.131800, 0.105440], 'p_i': 20, 'u_i': 4.2680},
        {'id': 2, 'e_m': 0.780802, 'e_o_k': [0.116135, 0.092908, 0.074327, 0.059461, 0.047569], 'p_i': 40, 'u_i': 4.9110},
        {'id': 3, 'e_m': 26.630915, 'e_o_k': [3.609229, 2.887383, 2.309907, 1.847925, 1.478340, 1.182672], 'p_i': 80, 'u_i': 1.5555},
        {'id': 4, 'e_m': 1.850169, 'e_o_k': [0.379133, 0.303306, 0.242645], 'p_i': 20, 'u_i': 1.9189},
        {'id': 5, 'e_m': 11.423752, 'e_o_k': [3.173265, 2.538612], 'p_i': 80, 'u_i': 3.1608},
    ]
    B_BUDGET = 110.399986
    return processors, tasks, B_BUDGET
