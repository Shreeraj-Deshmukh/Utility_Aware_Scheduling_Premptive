"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640011, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640011, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.399429, 'e_o_k': [0.166350, 0.133080, 0.106464, 0.085171, 0.068137], 'p_i': 10, 'u_i': 2.8237},
        {'id': 1, 'e_m': 2.463878, 'e_o_k': [1.916350, 1.533080], 'p_i': 20, 'u_i': 2.8601},
        {'id': 2, 'e_m': 8.416090, 'e_o_k': [3.991371, 3.193097, 2.554477, 2.043582], 'p_i': 40, 'u_i': 4.7969},
        {'id': 3, 'e_m': 34.116873, 'e_o_k': [14.208598, 11.366878, 9.093503, 7.274802, 5.819842], 'p_i': 80, 'u_i': 4.3760},
    ]
    B_BUDGET = 176.640011
    return processors, tasks, B_BUDGET
