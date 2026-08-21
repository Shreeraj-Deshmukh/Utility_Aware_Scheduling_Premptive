"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120003, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120003, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.706008, 'e_o_k': [0.784335, 0.627468], 'p_i': 10, 'u_i': 4.9296},
        {'id': 1, 'e_m': 5.892930, 'e_o_k': [0.479193, 0.383355, 0.306684, 0.245347, 0.196278, 0.157022], 'p_i': 20, 'u_i': 4.5772},
        {'id': 2, 'e_m': 17.713152, 'e_o_k': [1.580779, 1.264623, 1.011698, 0.809359, 0.647487], 'p_i': 40, 'u_i': 4.4816},
        {'id': 3, 'e_m': 21.392092, 'e_o_k': [2.173993, 1.739194, 1.391356, 1.113084], 'p_i': 80, 'u_i': 1.1432},
        {'id': 4, 'e_m': 3.323623, 'e_o_k': [0.337767, 0.270213, 0.216171, 0.172936], 'p_i': 20, 'u_i': 4.4630},
        {'id': 5, 'e_m': 2.896339, 'e_o_k': [0.294343, 0.235475, 0.188380, 0.150704], 'p_i': 10, 'u_i': 3.8428},
        {'id': 6, 'e_m': 2.882935, 'e_o_k': [0.257282, 0.205826, 0.164661, 0.131729, 0.105383], 'p_i': 20, 'u_i': 4.3035},
        {'id': 7, 'e_m': 2.491217, 'e_o_k': [0.202577, 0.162062, 0.129650, 0.103720, 0.082976, 0.066381], 'p_i': 20, 'u_i': 1.7239},
    ]
    B_BUDGET = 263.120003
    return processors, tasks, B_BUDGET
