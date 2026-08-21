"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639985, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639985, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.212074, 'e_o_k': [1.269223, 1.015378, 0.812303], 'p_i': 10, 'u_i': 4.4310},
        {'id': 1, 'e_m': 2.099648, 'e_o_k': [1.204716, 0.963773, 0.771018], 'p_i': 20, 'u_i': 4.5357},
        {'id': 2, 'e_m': 0.255502, 'e_o_k': [0.146599, 0.117279, 0.093824], 'p_i': 40, 'u_i': 3.5135},
        {'id': 3, 'e_m': 6.162213, 'e_o_k': [3.535696, 2.828557, 2.262845], 'p_i': 80, 'u_i': 3.8723},
        {'id': 4, 'e_m': 3.257255, 'e_o_k': [1.868917, 1.495134, 1.196107], 'p_i': 80, 'u_i': 1.1816},
        {'id': 5, 'e_m': 1.792700, 'e_o_k': [1.028598, 0.822879, 0.658303], 'p_i': 40, 'u_i': 3.3631},
        {'id': 6, 'e_m': 14.597411, 'e_o_k': [8.375564, 6.700451, 5.360361], 'p_i': 80, 'u_i': 2.0216},
        {'id': 7, 'e_m': 1.223941, 'e_o_k': [0.702261, 0.561809, 0.449447], 'p_i': 10, 'u_i': 3.3728},
    ]
    B_BUDGET = 176.639985
    return processors, tasks, B_BUDGET
