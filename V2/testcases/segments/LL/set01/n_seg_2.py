"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127821, 'e_o_k': [0.035506, 0.028405], 'p_i': 10, 'u_i': 1.1226},
        {'id': 1, 'e_m': 2.917468, 'e_o_k': [0.810408, 0.648326], 'p_i': 20, 'u_i': 3.8598},
        {'id': 2, 'e_m': 0.515015, 'e_o_k': [0.143060, 0.114448], 'p_i': 40, 'u_i': 4.6365},
        {'id': 3, 'e_m': 0.662519, 'e_o_k': [0.184033, 0.147226], 'p_i': 80, 'u_i': 1.0760},
        {'id': 4, 'e_m': 9.683938, 'e_o_k': [2.689983, 2.151986], 'p_i': 80, 'u_i': 3.5452},
        {'id': 5, 'e_m': 0.198293, 'e_o_k': [0.055081, 0.044065], 'p_i': 40, 'u_i': 3.7479},
        {'id': 6, 'e_m': 1.613164, 'e_o_k': [0.448101, 0.358481], 'p_i': 80, 'u_i': 4.4508},
        {'id': 7, 'e_m': 1.480331, 'e_o_k': [0.411203, 0.328963], 'p_i': 20, 'u_i': 2.7382},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET
