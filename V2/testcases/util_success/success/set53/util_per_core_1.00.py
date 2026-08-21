"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200001, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.795153, 'e_o_k': [0.132525, 0.106020], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 6.094129, 'e_o_k': [1.015688, 0.812550], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 4.978960, 'e_o_k': [0.444338, 0.355471, 0.284377, 0.227501, 0.182001], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 26.849317, 'e_o_k': [4.474886, 3.579909], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 4.592443, 'e_o_k': [0.373442, 0.298754, 0.239003, 0.191202, 0.152962, 0.122370], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 4.257314, 'e_o_k': [0.432654, 0.346123, 0.276899, 0.221519], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 7.151093, 'e_o_k': [0.726737, 0.581390, 0.465112, 0.372089], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 20.607256, 'e_o_k': [1.675714, 1.340571, 1.072457, 0.857965, 0.686372, 0.549098], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 239.200001
    return processors, tasks, B_BUDGET
