"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.176248, 'e_o_k': [0.604513, 0.483611], 'p_i': 10, 'u_i': 2.0210},
        {'id': 1, 'e_m': 1.214833, 'e_o_k': [0.337454, 0.269963], 'p_i': 20, 'u_i': 2.6755},
        {'id': 2, 'e_m': 1.222123, 'e_o_k': [0.206999, 0.165599, 0.132479, 0.105984], 'p_i': 40, 'u_i': 1.9112},
        {'id': 3, 'e_m': 7.286441, 'e_o_k': [1.083776, 0.867021, 0.693616, 0.554893, 0.443915], 'p_i': 80, 'u_i': 4.0850},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
