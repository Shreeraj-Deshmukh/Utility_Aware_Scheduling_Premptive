"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520002, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520002, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1034, "set": 34, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.329160, 'e_o_k': [0.040470, 0.032376, 0.025901], 'p_i': 10, 'u_i': 1.2368},
        {'id': 1, 'e_m': 1.718036, 'e_o_k': [0.139705, 0.111764, 0.089411, 0.071529, 0.057223, 0.045779], 'p_i': 20, 'u_i': 2.8306},
        {'id': 2, 'e_m': 16.892589, 'e_o_k': [2.076958, 1.661566, 1.329253], 'p_i': 40, 'u_i': 2.9234},
        {'id': 3, 'e_m': 11.145724, 'e_o_k': [1.370376, 1.096301, 0.877041], 'p_i': 80, 'u_i': 3.7707},
        {'id': 4, 'e_m': 3.994684, 'e_o_k': [0.491150, 0.392920, 0.314336], 'p_i': 20, 'u_i': 1.9627},
        {'id': 5, 'e_m': 4.907072, 'e_o_k': [0.817845, 0.654276], 'p_i': 40, 'u_i': 4.9296},
        {'id': 6, 'e_m': 0.042566, 'e_o_k': [0.003461, 0.002769, 0.002215, 0.001772, 0.001418, 0.001134], 'p_i': 40, 'u_i': 4.5772},
        {'id': 7, 'e_m': 1.960708, 'e_o_k': [0.174980, 0.139984, 0.111987, 0.089590, 0.071672], 'p_i': 10, 'u_i': 4.4816},
    ]
    B_BUDGET = 143.520002
    return processors, tasks, B_BUDGET
