"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.635145, 'e_o_k': [0.357135, 0.285708, 0.228567, 0.182853, 0.146283, 0.117026], 'p_i': 10, 'u_i': 3.8653},
        {'id': 1, 'e_m': 6.890535, 'e_o_k': [1.411995, 1.129596, 0.903677], 'p_i': 20, 'u_i': 1.8068},
        {'id': 2, 'e_m': 1.050998, 'e_o_k': [0.291944, 0.233555], 'p_i': 40, 'u_i': 1.4573},
        {'id': 3, 'e_m': 13.254707, 'e_o_k': [1.971488, 1.577190, 1.261752, 1.009402, 0.807521], 'p_i': 80, 'u_i': 1.2598},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
