"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.573508, 'e_o_k': [0.097139, 0.077711, 0.062169, 0.049735], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 1.886878, 'e_o_k': [0.319593, 0.255674, 0.204540, 0.163632], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 2.675239, 'e_o_k': [0.453123, 0.362498, 0.289999, 0.231999], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 8.484623, 'e_o_k': [1.437097, 1.149678, 0.919742, 0.735794], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 0.549748, 'e_o_k': [0.093115, 0.074492, 0.059593, 0.047675], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.074482, 'e_o_k': [0.012616, 0.010092, 0.008074, 0.006459], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 1.648956, 'e_o_k': [0.279295, 0.223436, 0.178749, 0.142999], 'p_i': 80, 'u_i': 2.9271},
        {'id': 7, 'e_m': 1.883445, 'e_o_k': [0.319012, 0.255209, 0.204167, 0.163334], 'p_i': 80, 'u_i': 1.9023},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET
