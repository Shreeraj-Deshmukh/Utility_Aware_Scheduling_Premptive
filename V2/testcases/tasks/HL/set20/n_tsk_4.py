"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.135760, 'e_o_k': [0.847492, 0.677993, 0.542395], 'p_i': 10, 'u_i': 2.1828},
        {'id': 1, 'e_m': 2.474534, 'e_o_k': [0.507077, 0.405661, 0.324529], 'p_i': 20, 'u_i': 3.4051},
        {'id': 2, 'e_m': 6.247662, 'e_o_k': [1.058208, 0.846567, 0.677253, 0.541803], 'p_i': 40, 'u_i': 2.6596},
        {'id': 3, 'e_m': 8.520465, 'e_o_k': [1.154760, 0.923808, 0.739046, 0.591237, 0.472990, 0.378392], 'p_i': 80, 'u_i': 2.1030},
    ]
    B_BUDGET = 110.400009
    return processors, tasks, B_BUDGET
