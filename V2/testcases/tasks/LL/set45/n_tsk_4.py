"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.110152, 'e_o_k': [0.030598, 0.024478], 'p_i': 10, 'u_i': 3.8084},
        {'id': 1, 'e_m': 1.382030, 'e_o_k': [0.205561, 0.164449, 0.131559, 0.105247, 0.084198], 'p_i': 20, 'u_i': 2.8237},
        {'id': 2, 'e_m': 0.048486, 'e_o_k': [0.013468, 0.010775], 'p_i': 40, 'u_i': 2.8601},
        {'id': 3, 'e_m': 25.493694, 'e_o_k': [4.318038, 3.454430, 2.763544, 2.210835], 'p_i': 80, 'u_i': 4.7969},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
