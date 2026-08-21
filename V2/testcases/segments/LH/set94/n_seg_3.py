"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1094, "set": 94, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.333816, 'e_o_k': [0.191534, 0.153227, 0.122582], 'p_i': 10, 'u_i': 1.6879},
        {'id': 1, 'e_m': 0.511403, 'e_o_k': [0.293428, 0.234742, 0.187794], 'p_i': 20, 'u_i': 2.2588},
        {'id': 2, 'e_m': 2.476328, 'e_o_k': [1.420844, 1.136675, 0.909340], 'p_i': 40, 'u_i': 4.0829},
        {'id': 3, 'e_m': 3.763800, 'e_o_k': [2.159558, 1.727646, 1.382117], 'p_i': 80, 'u_i': 1.6866},
        {'id': 4, 'e_m': 0.262962, 'e_o_k': [0.150880, 0.120704, 0.096563], 'p_i': 40, 'u_i': 3.5950},
        {'id': 5, 'e_m': 7.850730, 'e_o_k': [4.504517, 3.603614, 2.882891], 'p_i': 80, 'u_i': 4.2025},
        {'id': 6, 'e_m': 3.101814, 'e_o_k': [1.779730, 1.423784, 1.139027], 'p_i': 40, 'u_i': 3.6883},
        {'id': 7, 'e_m': 3.987120, 'e_o_k': [2.287692, 1.830153, 1.464123], 'p_i': 80, 'u_i': 1.6967},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET
