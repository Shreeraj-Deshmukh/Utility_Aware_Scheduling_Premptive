"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.131316, 'e_o_k': [0.314254, 0.251404], 'p_i': 10, 'u_i': 4.8131},
        {'id': 1, 'e_m': 6.732434, 'e_o_k': [1.001373, 0.801099, 0.640879, 0.512703, 0.410163], 'p_i': 20, 'u_i': 1.8577},
        {'id': 2, 'e_m': 7.823287, 'e_o_k': [1.603133, 1.282506, 1.026005], 'p_i': 40, 'u_i': 4.0468},
        {'id': 3, 'e_m': 12.373163, 'e_o_k': [1.840368, 1.472294, 1.177836, 0.942268, 0.753815], 'p_i': 80, 'u_i': 2.5682},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET
