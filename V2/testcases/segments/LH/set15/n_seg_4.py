"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.106037, 'e_o_k': [0.524543, 0.419635, 0.335708, 0.268566], 'p_i': 10, 'u_i': 4.4310},
        {'id': 1, 'e_m': 1.049824, 'e_o_k': [0.497884, 0.398307, 0.318646, 0.254917], 'p_i': 20, 'u_i': 4.5357},
        {'id': 2, 'e_m': 0.127751, 'e_o_k': [0.060586, 0.048469, 0.038775, 0.031020], 'p_i': 40, 'u_i': 3.5135},
        {'id': 3, 'e_m': 3.081106, 'e_o_k': [1.461229, 1.168983, 0.935187, 0.748149], 'p_i': 80, 'u_i': 3.8723},
        {'id': 4, 'e_m': 1.628628, 'e_o_k': [0.772384, 0.617907, 0.494326, 0.395461], 'p_i': 80, 'u_i': 1.1816},
        {'id': 5, 'e_m': 0.896350, 'e_o_k': [0.425098, 0.340079, 0.272063, 0.217650], 'p_i': 40, 'u_i': 3.3631},
        {'id': 6, 'e_m': 7.298706, 'e_o_k': [3.461446, 2.769157, 2.215325, 1.772260], 'p_i': 80, 'u_i': 2.0216},
        {'id': 7, 'e_m': 0.611971, 'e_o_k': [0.290230, 0.232184, 0.185747, 0.148598], 'p_i': 10, 'u_i': 3.3728},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET
