"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.187361, 'e_o_k': [0.145726, 0.116580], 'p_i': 10, 'u_i': 2.6135},
        {'id': 1, 'e_m': 2.315211, 'e_o_k': [0.878571, 0.702857, 0.562286, 0.449828, 0.359863, 0.287890], 'p_i': 20, 'u_i': 2.8871},
        {'id': 2, 'e_m': 6.099264, 'e_o_k': [2.314535, 1.851628, 1.481303, 1.185042, 0.948034, 0.758427], 'p_i': 40, 'u_i': 2.4127},
        {'id': 3, 'e_m': 15.366236, 'e_o_k': [8.816693, 7.053354, 5.642684], 'p_i': 80, 'u_i': 1.2331},
        {'id': 4, 'e_m': 6.272564, 'e_o_k': [3.599012, 2.879209, 2.303368], 'p_i': 40, 'u_i': 3.8857},
        {'id': 5, 'e_m': 3.282594, 'e_o_k': [2.553128, 2.042503], 'p_i': 20, 'u_i': 4.4773},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
