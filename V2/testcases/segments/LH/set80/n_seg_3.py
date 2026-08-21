"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320006, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320006, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.128317, 'e_o_k': [0.073625, 0.058900, 0.047120], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.270038, 'e_o_k': [0.154940, 0.123952, 0.099162], 'p_i': 20, 'u_i': 2.1078},
        {'id': 2, 'e_m': 0.379369, 'e_o_k': [0.217671, 0.174137, 0.139309], 'p_i': 40, 'u_i': 4.2406},
        {'id': 3, 'e_m': 8.098303, 'e_o_k': [4.646567, 3.717254, 2.973803], 'p_i': 80, 'u_i': 1.1754},
        {'id': 4, 'e_m': 5.065594, 'e_o_k': [2.906488, 2.325191, 1.860153], 'p_i': 40, 'u_i': 3.4237},
        {'id': 5, 'e_m': 3.042472, 'e_o_k': [1.745680, 1.396544, 1.117235], 'p_i': 40, 'u_i': 1.7653},
        {'id': 6, 'e_m': 0.412620, 'e_o_k': [0.236749, 0.189399, 0.151519], 'p_i': 10, 'u_i': 3.9977},
        {'id': 7, 'e_m': 0.379795, 'e_o_k': [0.217915, 0.174332, 0.139466], 'p_i': 20, 'u_i': 1.6134},
    ]
    B_BUDGET = 88.320006
    return processors, tasks, B_BUDGET
