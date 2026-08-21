"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200006, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200006, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.799720, 'e_o_k': [0.222144, 0.177716], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 2.592762, 'e_o_k': [0.720212, 0.576169], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 1.461112, 'e_o_k': [0.405864, 0.324692], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 3.792245, 'e_o_k': [1.053401, 0.842721], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 0.519494, 'e_o_k': [0.144304, 0.115443], 'p_i': 40, 'u_i': 3.3706},
        {'id': 5, 'e_m': 0.710845, 'e_o_k': [0.197457, 0.157966], 'p_i': 20, 'u_i': 1.2465},
        {'id': 6, 'e_m': 1.584893, 'e_o_k': [0.440248, 0.352199], 'p_i': 40, 'u_i': 3.7304},
        {'id': 7, 'e_m': 0.183071, 'e_o_k': [0.050853, 0.040683], 'p_i': 10, 'u_i': 3.6440},
    ]
    B_BUDGET = 55.200006
    return processors, tasks, B_BUDGET
