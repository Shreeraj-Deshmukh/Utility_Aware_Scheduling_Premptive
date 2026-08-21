"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.059988, 'e_o_k': [0.012293, 0.009834, 0.007867], 'p_i': 10, 'u_i': 4.5752},
        {'id': 1, 'e_m': 3.128087, 'e_o_k': [0.529825, 0.423860, 0.339088, 0.271270], 'p_i': 20, 'u_i': 3.6570},
        {'id': 2, 'e_m': 5.020593, 'e_o_k': [0.850371, 0.680297, 0.544238, 0.435390], 'p_i': 40, 'u_i': 3.9951},
        {'id': 3, 'e_m': 8.966561, 'e_o_k': [1.837410, 1.469928, 1.175942], 'p_i': 80, 'u_i': 2.8657},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET
