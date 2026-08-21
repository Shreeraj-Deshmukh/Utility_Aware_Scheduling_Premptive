"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640007, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640007, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.838505, 'e_o_k': [2.207726, 1.766181], 'p_i': 10, 'u_i': 4.9667},
        {'id': 1, 'e_m': 0.364276, 'e_o_k': [0.151709, 0.121367, 0.097094, 0.077675, 0.062140], 'p_i': 20, 'u_i': 1.4132},
        {'id': 2, 'e_m': 1.483734, 'e_o_k': [0.851323, 0.681058, 0.544846], 'p_i': 40, 'u_i': 4.6321},
        {'id': 3, 'e_m': 0.441000, 'e_o_k': [0.183662, 0.146930, 0.117544, 0.094035, 0.075228], 'p_i': 80, 'u_i': 3.6983},
        {'id': 4, 'e_m': 5.872901, 'e_o_k': [2.445878, 1.956702, 1.565362, 1.252289, 1.001831], 'p_i': 20, 'u_i': 3.0670},
        {'id': 5, 'e_m': 12.934789, 'e_o_k': [10.060391, 8.048313], 'p_i': 80, 'u_i': 2.2547},
    ]
    B_BUDGET = 176.640007
    return processors, tasks, B_BUDGET
