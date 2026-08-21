"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199982, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199982, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.777998, 'e_o_k': [0.105440, 0.084352, 0.067482, 0.053985, 0.043188, 0.034551], 'p_i': 10, 'u_i': 3.2097},
        {'id': 1, 'e_m': 0.780808, 'e_o_k': [0.160002, 0.128001, 0.102401], 'p_i': 20, 'u_i': 3.3970},
        {'id': 2, 'e_m': 1.200644, 'e_o_k': [0.162721, 0.130176, 0.104141, 0.083313, 0.066650, 0.053320], 'p_i': 40, 'u_i': 4.0644},
        {'id': 3, 'e_m': 7.863449, 'e_o_k': [1.169599, 0.935679, 0.748543, 0.598835, 0.479068], 'p_i': 80, 'u_i': 4.4775},
        {'id': 4, 'e_m': 1.305076, 'e_o_k': [0.221049, 0.176840, 0.141472, 0.113177], 'p_i': 10, 'u_i': 1.6225},
        {'id': 5, 'e_m': 1.947436, 'e_o_k': [0.263932, 0.211145, 0.168916, 0.135133, 0.108106, 0.086485], 'p_i': 80, 'u_i': 1.5082},
    ]
    B_BUDGET = 55.199982
    return processors, tasks, B_BUDGET
