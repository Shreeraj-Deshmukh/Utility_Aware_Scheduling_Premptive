"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 32, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 32, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.505787, 'e_o_k': [0.140496, 0.112397], 'p_i': 10, 'u_i': 2.8942},
        {'id': 1, 'e_m': 0.195219, 'e_o_k': [0.040004, 0.032003, 0.025602], 'p_i': 20, 'u_i': 2.8199},
        {'id': 2, 'e_m': 10.184228, 'e_o_k': [2.828952, 2.263162], 'p_i': 40, 'u_i': 2.3051},
        {'id': 3, 'e_m': 6.561179, 'e_o_k': [0.889222, 0.711378, 0.569102, 0.455282, 0.364225, 0.291380], 'p_i': 80, 'u_i': 3.4682},
        {'id': 4, 'e_m': 4.539403, 'e_o_k': [1.260945, 1.008756], 'p_i': 20, 'u_i': 2.3430},
        {'id': 5, 'e_m': 6.765491, 'e_o_k': [1.145917, 0.916733, 0.733387, 0.586709], 'p_i': 80, 'u_i': 2.4597},
        {'id': 6, 'e_m': 1.084629, 'e_o_k': [0.161326, 0.129061, 0.103249, 0.082599, 0.066079], 'p_i': 20, 'u_i': 4.3978},
        {'id': 7, 'e_m': 0.372698, 'e_o_k': [0.076373, 0.061098, 0.048878], 'p_i': 10, 'u_i': 2.9826},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET
