"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.567565, 'e_o_k': [1.219218, 0.975374], 'p_i': 10, 'u_i': 1.2013},
        {'id': 1, 'e_m': 0.270439, 'e_o_k': [0.155170, 0.124136, 0.099309], 'p_i': 20, 'u_i': 4.4940},
        {'id': 2, 'e_m': 16.617201, 'e_o_k': [6.305860, 5.044688, 4.035750, 3.228600, 2.582880, 2.066304], 'p_i': 40, 'u_i': 4.9438},
        {'id': 3, 'e_m': 17.143319, 'e_o_k': [6.505509, 5.204408, 4.163526, 3.330821, 2.664657, 2.131725], 'p_i': 80, 'u_i': 2.3791},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
