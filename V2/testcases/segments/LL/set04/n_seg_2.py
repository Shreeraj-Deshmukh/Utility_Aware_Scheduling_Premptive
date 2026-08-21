"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.464878, 'e_o_k': [0.129133, 0.103306], 'p_i': 10, 'u_i': 1.2748},
        {'id': 1, 'e_m': 0.028439, 'e_o_k': [0.007900, 0.006320], 'p_i': 20, 'u_i': 3.8825},
        {'id': 2, 'e_m': 1.311997, 'e_o_k': [0.364444, 0.291555], 'p_i': 40, 'u_i': 3.8582},
        {'id': 3, 'e_m': 2.237336, 'e_o_k': [0.621482, 0.497186], 'p_i': 80, 'u_i': 1.6137},
        {'id': 4, 'e_m': 1.174834, 'e_o_k': [0.326343, 0.261074], 'p_i': 20, 'u_i': 2.7253},
        {'id': 5, 'e_m': 5.271494, 'e_o_k': [1.464304, 1.171443], 'p_i': 40, 'u_i': 1.4714},
        {'id': 6, 'e_m': 0.171228, 'e_o_k': [0.047563, 0.038051], 'p_i': 10, 'u_i': 2.9160},
        {'id': 7, 'e_m': 1.673435, 'e_o_k': [0.464843, 0.371875], 'p_i': 20, 'u_i': 4.4871},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET
