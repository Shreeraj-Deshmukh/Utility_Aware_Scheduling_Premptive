"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.074983, 'e_o_k': [0.220283, 0.176227, 0.140981], 'p_i': 10, 'u_i': 1.0606},
        {'id': 1, 'e_m': 0.207897, 'e_o_k': [0.042602, 0.034082, 0.027265], 'p_i': 20, 'u_i': 3.4010},
        {'id': 2, 'e_m': 0.505827, 'e_o_k': [0.103653, 0.082922, 0.066338], 'p_i': 40, 'u_i': 1.6455},
        {'id': 3, 'e_m': 11.981266, 'e_o_k': [2.455177, 1.964142, 1.571314], 'p_i': 80, 'u_i': 1.3745},
        {'id': 4, 'e_m': 0.627821, 'e_o_k': [0.128652, 0.102922, 0.082337], 'p_i': 40, 'u_i': 1.5038},
        {'id': 5, 'e_m': 3.196490, 'e_o_k': [0.655019, 0.524015, 0.419212], 'p_i': 40, 'u_i': 4.4242},
        {'id': 6, 'e_m': 0.856156, 'e_o_k': [0.175442, 0.140353, 0.112283], 'p_i': 40, 'u_i': 1.3856},
        {'id': 7, 'e_m': 0.053673, 'e_o_k': [0.010998, 0.008799, 0.007039], 'p_i': 20, 'u_i': 2.4453},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
