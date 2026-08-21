"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600013, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600013, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.269592, 'e_o_k': [0.433902, 0.347121, 0.277697, 0.222158], 'p_i': 10, 'u_i': 3.9517},
        {'id': 1, 'e_m': 0.186040, 'e_o_k': [0.016603, 0.013282, 0.010626, 0.008501, 0.006801], 'p_i': 20, 'u_i': 3.7467},
        {'id': 2, 'e_m': 2.607682, 'e_o_k': [0.232718, 0.186174, 0.148939, 0.119152, 0.095321], 'p_i': 40, 'u_i': 4.6120},
        {'id': 3, 'e_m': 1.055593, 'e_o_k': [0.175932, 0.140746], 'p_i': 80, 'u_i': 4.9202},
        {'id': 4, 'e_m': 2.366843, 'e_o_k': [0.394474, 0.315579], 'p_i': 80, 'u_i': 4.2451},
        {'id': 5, 'e_m': 1.362496, 'e_o_k': [0.227083, 0.181666], 'p_i': 10, 'u_i': 4.7909},
        {'id': 6, 'e_m': 3.186185, 'e_o_k': [0.323799, 0.259039, 0.207232, 0.165785], 'p_i': 10, 'u_i': 3.3523},
        {'id': 7, 'e_m': 0.035931, 'e_o_k': [0.003651, 0.002921, 0.002337, 0.001870], 'p_i': 40, 'u_i': 1.0347},
    ]
    B_BUDGET = 119.600013
    return processors, tasks, B_BUDGET
