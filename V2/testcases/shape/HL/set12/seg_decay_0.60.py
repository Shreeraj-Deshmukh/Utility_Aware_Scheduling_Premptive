"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400003, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.400003, "H": 80, "J": 25, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.147016, 'e_o_k': [0.358443, 0.215066], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 3.773755, 'e_o_k': [1.179299, 0.707579], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 5.350477, 'e_o_k': [1.364918, 0.818951, 0.491370], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 16.969247, 'e_o_k': [3.680007, 2.208004, 1.324802, 0.794881, 0.476929], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 1.099497, 'e_o_k': [0.280484, 0.168290, 0.100974], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.148964, 'e_o_k': [0.032305, 0.019383, 0.011630, 0.006978, 0.004187], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 3.297912, 'e_o_k': [0.691862, 0.415117, 0.249070, 0.149442, 0.089665, 0.053799], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 3.766890, 'e_o_k': [0.816900, 0.490140, 0.294084, 0.176450, 0.105870], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 110.400003
    return processors, tasks, B_BUDGET
