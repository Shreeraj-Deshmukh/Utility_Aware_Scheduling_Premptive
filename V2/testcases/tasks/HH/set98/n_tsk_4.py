"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.512026, 'e_o_k': [1.332736, 1.066189, 0.852951, 0.682361, 0.545889, 0.436711], 'p_i': 10, 'u_i': 4.8035},
        {'id': 1, 'e_m': 2.438156, 'e_o_k': [1.015415, 0.812332, 0.649865, 0.519892, 0.415914], 'p_i': 20, 'u_i': 1.9119},
        {'id': 2, 'e_m': 9.105282, 'e_o_k': [7.081886, 5.665509], 'p_i': 40, 'u_i': 3.5492},
        {'id': 3, 'e_m': 7.940603, 'e_o_k': [6.176025, 4.940820], 'p_i': 80, 'u_i': 2.1494},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET
