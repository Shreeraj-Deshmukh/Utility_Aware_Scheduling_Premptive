"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.086163, 'e_o_k': [0.161555, 0.129244, 0.103395, 0.082716, 0.066173], 'p_i': 10, 'u_i': 4.6924},
        {'id': 1, 'e_m': 1.935110, 'e_o_k': [0.262261, 0.209809, 0.167847, 0.134278, 0.107422, 0.085938], 'p_i': 20, 'u_i': 3.7468},
        {'id': 2, 'e_m': 13.824883, 'e_o_k': [3.840245, 3.072196], 'p_i': 40, 'u_i': 3.5829},
        {'id': 3, 'e_m': 19.920487, 'e_o_k': [2.699780, 2.159824, 1.727859, 1.382287, 1.105830, 0.884664], 'p_i': 80, 'u_i': 3.3883},
    ]
    B_BUDGET = 110.400008
    return processors, tasks, B_BUDGET
