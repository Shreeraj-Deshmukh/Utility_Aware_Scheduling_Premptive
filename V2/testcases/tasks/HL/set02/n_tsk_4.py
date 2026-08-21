"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.562930, 'e_o_k': [0.320273, 0.256218, 0.204974], 'p_i': 10, 'u_i': 2.1098},
        {'id': 1, 'e_m': 4.518335, 'e_o_k': [0.925888, 0.740711, 0.592569], 'p_i': 20, 'u_i': 3.5044},
        {'id': 2, 'e_m': 13.019260, 'e_o_k': [1.764472, 1.411577, 1.129262, 0.903409, 0.722728, 0.578182], 'p_i': 40, 'u_i': 1.3726},
        {'id': 3, 'e_m': 7.384699, 'e_o_k': [1.098390, 0.878712, 0.702970, 0.562376, 0.449901], 'p_i': 80, 'u_i': 3.0405},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET
