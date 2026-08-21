"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 22, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 22, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1069, "set": 69, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.028851, 'e_o_k': [0.005912, 0.004730, 0.003784], 'p_i': 10, 'u_i': 3.1857},
        {'id': 1, 'e_m': 0.425044, 'e_o_k': [0.087099, 0.069679, 0.055743], 'p_i': 20, 'u_i': 3.0673},
        {'id': 2, 'e_m': 0.371477, 'e_o_k': [0.076122, 0.060898, 0.048718], 'p_i': 40, 'u_i': 1.1608},
        {'id': 3, 'e_m': 3.599048, 'e_o_k': [0.737510, 0.590008, 0.472006], 'p_i': 80, 'u_i': 3.0557},
        {'id': 4, 'e_m': 5.420557, 'e_o_k': [1.110770, 0.888616, 0.710893], 'p_i': 80, 'u_i': 1.7105},
        {'id': 5, 'e_m': 15.171358, 'e_o_k': [3.108885, 2.487108, 1.989686], 'p_i': 80, 'u_i': 2.7562},
        {'id': 6, 'e_m': 0.633743, 'e_o_k': [0.129865, 0.103892, 0.083114], 'p_i': 20, 'u_i': 4.1777},
        {'id': 7, 'e_m': 2.600128, 'e_o_k': [0.532813, 0.426251, 0.341000], 'p_i': 80, 'u_i': 1.3396},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
