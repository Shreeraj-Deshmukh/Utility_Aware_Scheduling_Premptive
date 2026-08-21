"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200003, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200003, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.711832, 'e_o_k': [0.152769, 0.122216, 0.097772, 0.078218, 0.062574], 'p_i': 10, 'u_i': 1.3735},
        {'id': 1, 'e_m': 6.685588, 'e_o_k': [0.679430, 0.543544, 0.434835, 0.347868], 'p_i': 20, 'u_i': 1.0216},
        {'id': 2, 'e_m': 15.017765, 'e_o_k': [1.846446, 1.477157, 1.181726], 'p_i': 40, 'u_i': 2.5479},
        {'id': 3, 'e_m': 27.743101, 'e_o_k': [2.255977, 1.804781, 1.443825, 1.155060, 0.924048, 0.739239], 'p_i': 80, 'u_i': 1.6473},
        {'id': 4, 'e_m': 6.476530, 'e_o_k': [0.577986, 0.462389, 0.369911, 0.295929, 0.236743], 'p_i': 80, 'u_i': 4.0690},
        {'id': 5, 'e_m': 5.433609, 'e_o_k': [0.668067, 0.534453, 0.427563], 'p_i': 20, 'u_i': 4.0670},
        {'id': 6, 'e_m': 2.465168, 'e_o_k': [0.220000, 0.176000, 0.140800, 0.112640, 0.090112], 'p_i': 20, 'u_i': 1.4405},
        {'id': 7, 'e_m': 5.928181, 'e_o_k': [0.482060, 0.385648, 0.308518, 0.246815, 0.197452, 0.157961], 'p_i': 20, 'u_i': 4.2490},
    ]
    B_BUDGET = 239.200003
    return processors, tasks, B_BUDGET
