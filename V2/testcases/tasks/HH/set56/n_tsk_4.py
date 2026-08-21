"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.146111, 'e_o_k': [2.378916, 1.903133, 1.522506], 'p_i': 10, 'u_i': 2.4204},
        {'id': 1, 'e_m': 0.534383, 'e_o_k': [0.202787, 0.162229, 0.129783, 0.103827, 0.083061, 0.066449], 'p_i': 20, 'u_i': 4.6440},
        {'id': 2, 'e_m': 2.973342, 'e_o_k': [1.128318, 0.902654, 0.722123, 0.577699, 0.462159, 0.369727], 'p_i': 40, 'u_i': 4.0628},
        {'id': 3, 'e_m': 22.746898, 'e_o_k': [9.473363, 7.578690, 6.062952, 4.850362, 3.880290], 'p_i': 80, 'u_i': 1.2692},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET
