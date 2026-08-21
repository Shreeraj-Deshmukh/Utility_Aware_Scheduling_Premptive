"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.467876, 'e_o_k': [0.063410, 0.050728, 0.040583, 0.032466, 0.025973, 0.020778], 'p_i': 10, 'u_i': 2.7067},
        {'id': 1, 'e_m': 1.187129, 'e_o_k': [0.160889, 0.128711, 0.102969, 0.082375, 0.065900, 0.052720], 'p_i': 20, 'u_i': 4.2680},
        {'id': 2, 'e_m': 0.390401, 'e_o_k': [0.058068, 0.046454, 0.037163, 0.029731, 0.023785], 'p_i': 40, 'u_i': 4.9110},
        {'id': 3, 'e_m': 13.315458, 'e_o_k': [1.804615, 1.443692, 1.154953, 0.923963, 0.739170, 0.591336], 'p_i': 80, 'u_i': 1.5555},
        {'id': 4, 'e_m': 0.925085, 'e_o_k': [0.189567, 0.151653, 0.121323], 'p_i': 20, 'u_i': 1.9189},
        {'id': 5, 'e_m': 5.711876, 'e_o_k': [1.586632, 1.269306], 'p_i': 80, 'u_i': 3.1608},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET
