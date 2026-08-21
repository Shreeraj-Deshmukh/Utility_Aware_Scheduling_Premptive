"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 33, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 33, "factor": "regime", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_split", "util_per_core": 0.2, "value": "LL"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.030044, 'e_o_k': [0.211075, 0.168860, 0.135088], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.169513, 'e_o_k': [0.028712, 0.022969, 0.018375, 0.014700], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 7.923597, 'e_o_k': [1.342073, 1.073658, 0.858926, 0.687141], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 0.881446, 'e_o_k': [0.131105, 0.104884, 0.083907, 0.067126, 0.053701], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.392495, 'e_o_k': [0.080429, 0.064343, 0.051475], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.407213, 'e_o_k': [0.068972, 0.055178, 0.044142, 0.035314], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.082726, 'e_o_k': [0.012305, 0.009844, 0.007875, 0.006300, 0.005040], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.494838, 'e_o_k': [0.083814, 0.067051, 0.053641, 0.042913], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
