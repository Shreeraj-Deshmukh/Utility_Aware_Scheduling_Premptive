"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319988, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319988, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1027, "set": 27, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.165491, 'e_o_k': [1.684271, 1.347417], 'p_i': 10, 'u_i': 4.6007},
        {'id': 1, 'e_m': 0.088973, 'e_o_k': [0.037055, 0.029644, 0.023715, 0.018972, 0.015178], 'p_i': 20, 'u_i': 4.4928},
        {'id': 2, 'e_m': 1.326107, 'e_o_k': [0.503228, 0.402583, 0.322066, 0.257653, 0.206122, 0.164898], 'p_i': 40, 'u_i': 4.0915},
        {'id': 3, 'e_m': 0.609452, 'e_o_k': [0.231274, 0.185019, 0.148015, 0.118412, 0.094730, 0.075784], 'p_i': 80, 'u_i': 4.3648},
        {'id': 4, 'e_m': 1.901509, 'e_o_k': [1.478952, 1.183161], 'p_i': 80, 'u_i': 3.7706},
        {'id': 5, 'e_m': 2.289249, 'e_o_k': [0.868719, 0.694976, 0.555980, 0.444784, 0.355827, 0.284662], 'p_i': 20, 'u_i': 4.9150},
    ]
    B_BUDGET = 88.319988
    return processors, tasks, B_BUDGET
