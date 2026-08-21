"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.218931, 'e_o_k': [0.436255, 0.349004, 0.279203, 0.223362, 0.178690, 0.142952], 'p_i': 10, 'u_i': 2.6491},
        {'id': 1, 'e_m': 5.141798, 'e_o_k': [1.053647, 0.842918, 0.674334], 'p_i': 20, 'u_i': 3.0546},
        {'id': 2, 'e_m': 7.765348, 'e_o_k': [1.155008, 0.924006, 0.739205, 0.591364, 0.473091], 'p_i': 40, 'u_i': 3.4882},
        {'id': 3, 'e_m': 2.150661, 'e_o_k': [0.319887, 0.255909, 0.204727, 0.163782, 0.131026], 'p_i': 80, 'u_i': 2.0277},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
