"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.511173, 'e_o_k': [0.309667, 0.247733, 0.198187], 'p_i': 10, 'u_i': 2.2612},
        {'id': 1, 'e_m': 3.773415, 'e_o_k': [0.639129, 0.511303, 0.409042, 0.327234], 'p_i': 20, 'u_i': 2.3936},
        {'id': 2, 'e_m': 12.214956, 'e_o_k': [2.068929, 1.655143, 1.324114, 1.059292], 'p_i': 40, 'u_i': 4.7316},
        {'id': 3, 'e_m': 12.387043, 'e_o_k': [2.098076, 1.678461, 1.342769, 1.074215], 'p_i': 80, 'u_i': 1.7602},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET
