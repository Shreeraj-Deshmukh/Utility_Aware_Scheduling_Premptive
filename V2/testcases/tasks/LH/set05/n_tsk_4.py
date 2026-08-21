"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.861356, 'e_o_k': [0.326865, 0.261492, 0.209194, 0.167355, 0.133884, 0.107107], 'p_i': 10, 'u_i': 3.5509},
        {'id': 1, 'e_m': 0.314912, 'e_o_k': [0.149348, 0.119479, 0.095583, 0.076466], 'p_i': 20, 'u_i': 2.4298},
        {'id': 2, 'e_m': 5.515709, 'e_o_k': [3.164751, 2.531801, 2.025441], 'p_i': 40, 'u_i': 2.9531},
        {'id': 3, 'e_m': 12.818090, 'e_o_k': [4.864181, 3.891345, 3.113076, 2.490461, 1.992369, 1.593895], 'p_i': 80, 'u_i': 4.5727},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
