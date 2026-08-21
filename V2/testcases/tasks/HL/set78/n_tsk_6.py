"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400013, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400013, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.006173, 'e_o_k': [0.509176, 0.407341, 0.325872, 0.260698], 'p_i': 10, 'u_i': 1.9112},
        {'id': 1, 'e_m': 1.831089, 'e_o_k': [0.272354, 0.217883, 0.174306, 0.139445, 0.111556], 'p_i': 20, 'u_i': 4.0850},
        {'id': 2, 'e_m': 1.499507, 'e_o_k': [0.253982, 0.203185, 0.162548, 0.130039], 'p_i': 40, 'u_i': 1.7025},
        {'id': 3, 'e_m': 22.962509, 'e_o_k': [3.415414, 2.732331, 2.185865, 1.748692, 1.398953], 'p_i': 80, 'u_i': 2.0058},
        {'id': 4, 'e_m': 0.417577, 'e_o_k': [0.115994, 0.092795], 'p_i': 10, 'u_i': 3.5722},
        {'id': 5, 'e_m': 3.324123, 'e_o_k': [0.563029, 0.450423, 0.360339, 0.288271], 'p_i': 80, 'u_i': 1.2384},
    ]
    B_BUDGET = 110.400013
    return processors, tasks, B_BUDGET
