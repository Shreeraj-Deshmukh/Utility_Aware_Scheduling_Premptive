"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.439386, 'e_o_k': [0.341745, 0.273396], 'p_i': 10, 'u_i': 3.0447},
        {'id': 1, 'e_m': 3.381221, 'e_o_k': [2.629839, 2.103871], 'p_i': 20, 'u_i': 2.1118},
        {'id': 2, 'e_m': 4.501107, 'e_o_k': [3.500861, 2.800689], 'p_i': 40, 'u_i': 4.2305},
        {'id': 3, 'e_m': 1.296672, 'e_o_k': [1.008523, 0.806818], 'p_i': 80, 'u_i': 2.0791},
        {'id': 4, 'e_m': 14.537940, 'e_o_k': [11.307287, 9.045829], 'p_i': 80, 'u_i': 1.4810},
        {'id': 5, 'e_m': 7.948216, 'e_o_k': [6.181946, 4.945556], 'p_i': 80, 'u_i': 3.5439},
        {'id': 6, 'e_m': 7.236118, 'e_o_k': [5.628092, 4.502474], 'p_i': 80, 'u_i': 1.8113},
        {'id': 7, 'e_m': 0.867358, 'e_o_k': [0.674612, 0.539689], 'p_i': 10, 'u_i': 4.9983},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET
