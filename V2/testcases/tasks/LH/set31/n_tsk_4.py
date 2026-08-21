"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.446847, 'e_o_k': [0.211919, 0.169536, 0.135628, 0.108503], 'p_i': 10, 'u_i': 2.2748},
        {'id': 1, 'e_m': 1.831443, 'e_o_k': [0.868571, 0.694857, 0.555885, 0.444708], 'p_i': 20, 'u_i': 3.5166},
        {'id': 2, 'e_m': 0.329386, 'e_o_k': [0.156213, 0.124970, 0.099976, 0.079981], 'p_i': 40, 'u_i': 2.8575},
        {'id': 3, 'e_m': 20.440676, 'e_o_k': [8.512895, 6.810316, 5.448253, 4.358602, 3.486882], 'p_i': 80, 'u_i': 2.8209},
    ]
    B_BUDGET = 88.319995
    return processors, tasks, B_BUDGET
