"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199985, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199985, "H": 80, "J": 36, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.969434, 'e_o_k': [0.301772, 0.241417, 0.193134, 0.154507], 'p_i': 10, 'u_i': 4.7936},
        {'id': 1, 'e_m': 6.147706, 'e_o_k': [1.024618, 0.819694], 'p_i': 20, 'u_i': 3.8633},
        {'id': 2, 'e_m': 19.425776, 'e_o_k': [2.388415, 1.910732, 1.528586], 'p_i': 40, 'u_i': 3.6436},
        {'id': 3, 'e_m': 29.869010, 'e_o_k': [2.665607, 2.132485, 1.705988, 1.364791, 1.091832], 'p_i': 80, 'u_i': 2.9643},
        {'id': 4, 'e_m': 0.057727, 'e_o_k': [0.005152, 0.004121, 0.003297, 0.002638, 0.002110], 'p_i': 10, 'u_i': 2.7604},
        {'id': 5, 'e_m': 8.231406, 'e_o_k': [1.012058, 0.809646, 0.647717], 'p_i': 20, 'u_i': 2.8703},
        {'id': 6, 'e_m': 0.019437, 'e_o_k': [0.002390, 0.001912, 0.001529], 'p_i': 10, 'u_i': 2.8894},
        {'id': 7, 'e_m': 9.390200, 'e_o_k': [1.154533, 0.923626, 0.738901], 'p_i': 80, 'u_i': 1.0820},
    ]
    B_BUDGET = 239.199985
    return processors, tasks, B_BUDGET
