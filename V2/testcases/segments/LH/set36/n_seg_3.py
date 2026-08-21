"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471162, 'e_o_k': [0.270339, 0.216271, 0.173017], 'p_i': 10, 'u_i': 2.0085},
        {'id': 1, 'e_m': 0.359296, 'e_o_k': [0.206153, 0.164923, 0.131938], 'p_i': 20, 'u_i': 4.1252},
        {'id': 2, 'e_m': 0.377372, 'e_o_k': [0.216525, 0.173220, 0.138576], 'p_i': 40, 'u_i': 4.4037},
        {'id': 3, 'e_m': 2.056648, 'e_o_k': [1.180044, 0.944035, 0.755228], 'p_i': 80, 'u_i': 1.7011},
        {'id': 4, 'e_m': 7.946467, 'e_o_k': [4.559448, 3.647559, 2.918047], 'p_i': 40, 'u_i': 1.8442},
        {'id': 5, 'e_m': 1.594191, 'e_o_k': [0.914700, 0.731760, 0.585408], 'p_i': 40, 'u_i': 2.3108},
        {'id': 6, 'e_m': 0.525986, 'e_o_k': [0.301796, 0.241436, 0.193149], 'p_i': 10, 'u_i': 1.0383},
        {'id': 7, 'e_m': 0.346460, 'e_o_k': [0.198789, 0.159031, 0.127225], 'p_i': 40, 'u_i': 2.0614},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET
