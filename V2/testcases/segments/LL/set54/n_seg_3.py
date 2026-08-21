"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.19999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.19999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.030044, 'e_o_k': [0.211075, 0.168860, 0.135088], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.169513, 'e_o_k': [0.034736, 0.027789, 0.022231], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 7.923597, 'e_o_k': [1.623688, 1.298950, 1.039160], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 0.881446, 'e_o_k': [0.180624, 0.144499, 0.115600], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.392495, 'e_o_k': [0.080429, 0.064343, 0.051475], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.407213, 'e_o_k': [0.083445, 0.066756, 0.053405], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.082726, 'e_o_k': [0.016952, 0.013562, 0.010849], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.494838, 'e_o_k': [0.101401, 0.081121, 0.064897], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 55.199990
    return processors, tasks, B_BUDGET
