"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319987, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 88.319987, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.471162, 'e_o_k': [0.196224, 0.156979, 0.125583, 0.100467, 0.080373], 'p_i': 10, 'u_i': 2.7521},
        {'id': 1, 'e_m': 0.359296, 'e_o_k': [0.206153, 0.164923, 0.131938], 'p_i': 20, 'u_i': 3.2813},
        {'id': 2, 'e_m': 0.377372, 'e_o_k': [0.143204, 0.114563, 0.091651, 0.073321, 0.058656, 0.046925], 'p_i': 40, 'u_i': 2.6292},
        {'id': 3, 'e_m': 2.056648, 'e_o_k': [1.599615, 1.279692], 'p_i': 80, 'u_i': 2.5629},
        {'id': 4, 'e_m': 7.946467, 'e_o_k': [3.768650, 3.014920, 2.411936, 1.929549], 'p_i': 40, 'u_i': 3.2054},
        {'id': 5, 'e_m': 1.594191, 'e_o_k': [0.914700, 0.731760, 0.585408], 'p_i': 40, 'u_i': 3.3403},
        {'id': 6, 'e_m': 0.525986, 'e_o_k': [0.249452, 0.199561, 0.159649, 0.127719], 'p_i': 10, 'u_i': 2.8277},
        {'id': 7, 'e_m': 0.346460, 'e_o_k': [0.164310, 0.131448, 0.105159, 0.084127], 'p_i': 40, 'u_i': 2.5096},
    ]
    B_BUDGET = 88.319987
    return processors, tasks, B_BUDGET
