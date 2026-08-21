"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.128317, 'e_o_k': [0.035644, 0.028515], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.270038, 'e_o_k': [0.075011, 0.060008], 'p_i': 20, 'u_i': 2.1078},
        {'id': 2, 'e_m': 0.379369, 'e_o_k': [0.105380, 0.084304], 'p_i': 40, 'u_i': 4.2406},
        {'id': 3, 'e_m': 8.098303, 'e_o_k': [2.249528, 1.799623], 'p_i': 80, 'u_i': 1.1754},
        {'id': 4, 'e_m': 5.065594, 'e_o_k': [1.407109, 1.125688], 'p_i': 40, 'u_i': 3.4237},
        {'id': 5, 'e_m': 3.042472, 'e_o_k': [0.845131, 0.676105], 'p_i': 40, 'u_i': 1.7653},
        {'id': 6, 'e_m': 0.412620, 'e_o_k': [0.114617, 0.091693], 'p_i': 10, 'u_i': 3.9977},
        {'id': 7, 'e_m': 0.379795, 'e_o_k': [0.105499, 0.084399], 'p_i': 20, 'u_i': 1.6134},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET
