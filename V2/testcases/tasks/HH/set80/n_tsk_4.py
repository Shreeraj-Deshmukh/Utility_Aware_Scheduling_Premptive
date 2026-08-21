"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.817928, 'e_o_k': [1.336416, 1.069133, 0.855306, 0.684245], 'p_i': 10, 'u_i': 4.6156},
        {'id': 1, 'e_m': 6.495812, 'e_o_k': [3.080670, 2.464536, 1.971629, 1.577303], 'p_i': 20, 'u_i': 1.3815},
        {'id': 2, 'e_m': 6.225140, 'e_o_k': [3.571801, 2.857441, 2.285953], 'p_i': 40, 'u_i': 2.2542},
        {'id': 3, 'e_m': 3.023045, 'e_o_k': [1.147179, 0.917743, 0.734194, 0.587356, 0.469884, 0.375908], 'p_i': 80, 'u_i': 3.1493},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
