"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.086163, 'e_o_k': [0.452353, 0.361882, 0.289506, 0.231605, 0.185284], 'p_i': 10, 'u_i': 4.6924},
        {'id': 1, 'e_m': 1.935110, 'e_o_k': [0.734331, 0.587465, 0.469972, 0.375978, 0.300782, 0.240626], 'p_i': 20, 'u_i': 3.7468},
        {'id': 2, 'e_m': 13.824883, 'e_o_k': [10.752686, 8.602149], 'p_i': 40, 'u_i': 3.5829},
        {'id': 3, 'e_m': 19.920487, 'e_o_k': [7.559383, 6.047507, 4.838005, 3.870404, 3.096323, 2.477059], 'p_i': 80, 'u_i': 3.3883},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET
