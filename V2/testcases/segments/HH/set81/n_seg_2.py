"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640007, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640007, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.808019, 'e_o_k': [0.628459, 0.502767], 'p_i': 10, 'u_i': 4.1044},
        {'id': 1, 'e_m': 2.624685, 'e_o_k': [2.041422, 1.633137], 'p_i': 20, 'u_i': 3.5158},
        {'id': 2, 'e_m': 3.033921, 'e_o_k': [2.359716, 1.887773], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 20.140991, 'e_o_k': [15.665215, 12.532172], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 2.165693, 'e_o_k': [1.684428, 1.347543], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.136094, 'e_o_k': [0.105851, 0.084681], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 3.875810, 'e_o_k': [3.014519, 2.411615], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.483689, 'e_o_k': [0.376202, 0.300962], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 176.640007
    return processors, tasks, B_BUDGET
