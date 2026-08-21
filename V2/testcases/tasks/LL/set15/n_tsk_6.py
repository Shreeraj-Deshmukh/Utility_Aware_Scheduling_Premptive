"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.457470, 'e_o_k': [0.216782, 0.173426, 0.138741, 0.110992, 0.088794], 'p_i': 10, 'u_i': 3.3568},
        {'id': 1, 'e_m': 1.318732, 'e_o_k': [0.223362, 0.178690, 0.142952, 0.114362], 'p_i': 20, 'u_i': 2.9125},
        {'id': 2, 'e_m': 0.168487, 'e_o_k': [0.022835, 0.018268, 0.014614, 0.011691, 0.009353, 0.007482], 'p_i': 40, 'u_i': 4.1129},
        {'id': 3, 'e_m': 4.454265, 'e_o_k': [0.603677, 0.482941, 0.386353, 0.309082, 0.247266, 0.197813], 'p_i': 80, 'u_i': 4.6267},
        {'id': 4, 'e_m': 2.890958, 'e_o_k': [0.803044, 0.642435], 'p_i': 80, 'u_i': 4.4310},
        {'id': 5, 'e_m': 3.691560, 'e_o_k': [0.549078, 0.439262, 0.351410, 0.281128, 0.224902], 'p_i': 40, 'u_i': 4.5357},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
