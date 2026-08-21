"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.419252, 'e_o_k': [0.394237, 0.315389], 'p_i': 10, 'u_i': 4.9667},
        {'id': 1, 'e_m': 0.182138, 'e_o_k': [0.027091, 0.021673, 0.017338, 0.013871, 0.011096], 'p_i': 20, 'u_i': 1.4132},
        {'id': 2, 'e_m': 0.741867, 'e_o_k': [0.152022, 0.121618, 0.097294], 'p_i': 40, 'u_i': 4.6321},
        {'id': 3, 'e_m': 0.220500, 'e_o_k': [0.032797, 0.026237, 0.020990, 0.016792, 0.013434], 'p_i': 80, 'u_i': 3.6983},
        {'id': 4, 'e_m': 2.936451, 'e_o_k': [0.436764, 0.349411, 0.279529, 0.223623, 0.178898], 'p_i': 20, 'u_i': 3.0670},
        {'id': 5, 'e_m': 6.467394, 'e_o_k': [1.796498, 1.437199], 'p_i': 80, 'u_i': 2.2547},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
