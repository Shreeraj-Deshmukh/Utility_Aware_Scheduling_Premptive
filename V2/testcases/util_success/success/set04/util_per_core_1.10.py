"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119999, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119999, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.426284, 'e_o_k': [0.404381, 0.323505], 'p_i': 10, 'u_i': 4.5314},
        {'id': 1, 'e_m': 3.100073, 'e_o_k': [0.252088, 0.201670, 0.161336, 0.129069, 0.103255, 0.082604], 'p_i': 20, 'u_i': 1.6938},
        {'id': 2, 'e_m': 17.841501, 'e_o_k': [1.592233, 1.273786, 1.019029, 0.815223, 0.652179], 'p_i': 40, 'u_i': 2.2421},
        {'id': 3, 'e_m': 6.919021, 'e_o_k': [1.153170, 0.922536], 'p_i': 80, 'u_i': 3.9578},
        {'id': 4, 'e_m': 1.725288, 'e_o_k': [0.153970, 0.123176, 0.098541, 0.078833, 0.063066], 'p_i': 10, 'u_i': 3.5176},
        {'id': 5, 'e_m': 3.494930, 'e_o_k': [0.311899, 0.249519, 0.199615, 0.159692, 0.127754], 'p_i': 10, 'u_i': 3.0954},
        {'id': 6, 'e_m': 12.028242, 'e_o_k': [1.478882, 1.183106, 0.946485], 'p_i': 40, 'u_i': 3.8180},
        {'id': 7, 'e_m': 17.884591, 'e_o_k': [1.596078, 1.276863, 1.021490, 0.817192, 0.653754], 'p_i': 40, 'u_i': 4.5821},
    ]
    B_BUDGET = 263.119999
    return processors, tasks, B_BUDGET
