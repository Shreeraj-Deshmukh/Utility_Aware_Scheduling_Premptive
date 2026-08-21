"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.496415, 'e_o_k': [0.188379, 0.150703, 0.120562, 0.096450, 0.077160, 0.061728], 'p_i': 10, 'u_i': 2.9591},
        {'id': 1, 'e_m': 2.106412, 'e_o_k': [0.877254, 0.701803, 0.561442, 0.449154, 0.359323], 'p_i': 20, 'u_i': 3.3490},
        {'id': 2, 'e_m': 6.598735, 'e_o_k': [5.132349, 4.105879], 'p_i': 40, 'u_i': 1.0216},
        {'id': 3, 'e_m': 2.207762, 'e_o_k': [1.266748, 1.013399, 0.810719], 'p_i': 80, 'u_i': 4.0085},
        {'id': 4, 'e_m': 0.027756, 'e_o_k': [0.015926, 0.012741, 0.010192], 'p_i': 20, 'u_i': 1.9931},
        {'id': 5, 'e_m': 4.086773, 'e_o_k': [2.344870, 1.875896, 1.500716], 'p_i': 80, 'u_i': 2.4773},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET
