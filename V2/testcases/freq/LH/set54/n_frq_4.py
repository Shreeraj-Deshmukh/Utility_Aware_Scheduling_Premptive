"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 33, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "freq", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 33, "factor": "n_frq", "n_frq": 4, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "freq", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.6, 0.8, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.030044, 'e_o_k': [0.591009, 0.472807, 0.378246], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.169513, 'e_o_k': [0.080392, 0.064314, 0.051451, 0.041161], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 7.923597, 'e_o_k': [3.757803, 3.006243, 2.404994, 1.923995], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 0.881446, 'e_o_k': [0.367094, 0.293676, 0.234940, 0.187952, 0.150362], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.392495, 'e_o_k': [0.225202, 0.180162, 0.144129], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.407213, 'e_o_k': [0.193123, 0.154498, 0.123599, 0.098879], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.082726, 'e_o_k': [0.034453, 0.027562, 0.022050, 0.017640, 0.014112], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.494838, 'e_o_k': [0.234679, 0.187744, 0.150195, 0.120156], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET
