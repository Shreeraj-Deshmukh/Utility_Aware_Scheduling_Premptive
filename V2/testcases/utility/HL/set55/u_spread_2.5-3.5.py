"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 28, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 28, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.362417, 'e_o_k': [0.320173, 0.256139, 0.204911, 0.163929, 0.131143, 0.104914], 'p_i': 10, 'u_i': 3.3783},
        {'id': 1, 'e_m': 1.818372, 'e_o_k': [0.372617, 0.298094, 0.238475], 'p_i': 20, 'u_i': 3.3969},
        {'id': 2, 'e_m': 2.018400, 'e_o_k': [0.413607, 0.330885, 0.264708], 'p_i': 40, 'u_i': 2.9337},
        {'id': 3, 'e_m': 10.977605, 'e_o_k': [2.249509, 1.799607, 1.439686], 'p_i': 80, 'u_i': 3.4918},
        {'id': 4, 'e_m': 5.439997, 'e_o_k': [0.809138, 0.647310, 0.517848, 0.414279, 0.331423], 'p_i': 80, 'u_i': 3.4690},
        {'id': 5, 'e_m': 0.284101, 'e_o_k': [0.048120, 0.038496, 0.030797, 0.024638], 'p_i': 10, 'u_i': 2.8812},
        {'id': 6, 'e_m': 1.455737, 'e_o_k': [0.404372, 0.323497], 'p_i': 40, 'u_i': 3.4883},
        {'id': 7, 'e_m': 6.094243, 'e_o_k': [1.032223, 0.825778, 0.660623, 0.528498], 'p_i': 40, 'u_i': 2.8245},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
