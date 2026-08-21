"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 30, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 30, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.003420, 'e_o_k': [0.169956, 0.135965, 0.108772, 0.087017], 'p_i': 10, 'u_i': 2.9497},
        {'id': 1, 'e_m': 0.071930, 'e_o_k': [0.012183, 0.009747, 0.007797, 0.006238], 'p_i': 20, 'u_i': 4.0162},
        {'id': 2, 'e_m': 2.182642, 'e_o_k': [0.324643, 0.259715, 0.207772, 0.166217, 0.132974], 'p_i': 40, 'u_i': 2.4556},
        {'id': 3, 'e_m': 0.960574, 'e_o_k': [0.196839, 0.157471, 0.125977], 'p_i': 80, 'u_i': 2.6856},
        {'id': 4, 'e_m': 1.684688, 'e_o_k': [0.250578, 0.200463, 0.160370, 0.128296, 0.102637], 'p_i': 40, 'u_i': 4.1517},
        {'id': 5, 'e_m': 0.701210, 'e_o_k': [0.143691, 0.114952, 0.091962], 'p_i': 20, 'u_i': 4.0598},
        {'id': 6, 'e_m': 3.408563, 'e_o_k': [0.698476, 0.558781, 0.447025], 'p_i': 80, 'u_i': 1.5979},
        {'id': 7, 'e_m': 1.097036, 'e_o_k': [0.185812, 0.148650, 0.118920, 0.095136], 'p_i': 10, 'u_i': 4.3280},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET
