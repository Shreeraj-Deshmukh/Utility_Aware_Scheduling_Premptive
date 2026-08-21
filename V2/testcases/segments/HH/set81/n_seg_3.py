"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.808019, 'e_o_k': [0.463617, 0.370894, 0.296715], 'p_i': 10, 'u_i': 4.1044},
        {'id': 1, 'e_m': 2.624685, 'e_o_k': [1.505967, 1.204773, 0.963819], 'p_i': 20, 'u_i': 3.5158},
        {'id': 2, 'e_m': 3.033921, 'e_o_k': [1.740774, 1.392620, 1.114096], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 20.140991, 'e_o_k': [11.556306, 9.245045, 7.396036], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 2.165693, 'e_o_k': [1.242611, 0.994089, 0.795271], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.136094, 'e_o_k': [0.078087, 0.062469, 0.049975], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 3.875810, 'e_o_k': [2.223825, 1.779060, 1.423248], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.483689, 'e_o_k': [0.277526, 0.222021, 0.177617], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
