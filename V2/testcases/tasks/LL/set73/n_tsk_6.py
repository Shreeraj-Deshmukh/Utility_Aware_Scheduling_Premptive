"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.20002, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1073, "set": 73, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.812906, 'e_o_k': [0.120911, 0.096729, 0.077383, 0.061906, 0.049525], 'p_i': 10, 'u_i': 4.4263},
        {'id': 1, 'e_m': 4.853783, 'e_o_k': [0.994628, 0.795702, 0.636562], 'p_i': 20, 'u_i': 1.7162},
        {'id': 2, 'e_m': 0.141292, 'e_o_k': [0.039248, 0.031398], 'p_i': 40, 'u_i': 1.4626},
        {'id': 3, 'e_m': 1.160648, 'e_o_k': [0.322402, 0.257922], 'p_i': 80, 'u_i': 2.2690},
        {'id': 4, 'e_m': 0.264860, 'e_o_k': [0.054275, 0.043420, 0.034736], 'p_i': 10, 'u_i': 1.2408},
        {'id': 5, 'e_m': 2.519507, 'e_o_k': [0.699863, 0.559891], 'p_i': 80, 'u_i': 2.2030},
    ]
    B_BUDGET = 55.200020
    return processors, tasks, B_BUDGET
