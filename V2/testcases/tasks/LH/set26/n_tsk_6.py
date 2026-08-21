"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320009, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320009, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.078517, 'e_o_k': [0.788751, 0.631001, 0.504801, 0.403841, 0.323072, 0.258458], 'p_i': 10, 'u_i': 2.2803},
        {'id': 1, 'e_m': 0.654353, 'e_o_k': [0.248312, 0.198650, 0.158920, 0.127136, 0.101709, 0.081367], 'p_i': 20, 'u_i': 3.9685},
        {'id': 2, 'e_m': 1.726347, 'e_o_k': [1.342714, 1.074171], 'p_i': 40, 'u_i': 1.4001},
        {'id': 3, 'e_m': 4.516779, 'e_o_k': [2.142104, 1.713683, 1.370946, 1.096757], 'p_i': 80, 'u_i': 2.1780},
        {'id': 4, 'e_m': 2.027836, 'e_o_k': [1.163512, 0.930810, 0.744648], 'p_i': 80, 'u_i': 3.8388},
        {'id': 5, 'e_m': 2.757147, 'e_o_k': [1.307590, 1.046072, 0.836858, 0.669486], 'p_i': 80, 'u_i': 1.0041},
    ]
    B_BUDGET = 88.320009
    return processors, tasks, B_BUDGET
