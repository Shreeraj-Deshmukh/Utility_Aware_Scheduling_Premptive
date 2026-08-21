"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.679997, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.679997, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.212074, 'e_o_k': [0.179879, 0.143903, 0.115122, 0.092098, 0.073678, 0.058943], 'p_i': 10, 'u_i': 4.6267},
        {'id': 1, 'e_m': 2.099648, 'e_o_k': [0.349941, 0.279953], 'p_i': 20, 'u_i': 4.4310},
        {'id': 2, 'e_m': 0.255502, 'e_o_k': [0.022802, 0.018241, 0.014593, 0.011675, 0.009340], 'p_i': 40, 'u_i': 4.5357},
        {'id': 3, 'e_m': 6.162213, 'e_o_k': [0.501091, 0.400873, 0.320698, 0.256558, 0.205247, 0.164197], 'p_i': 80, 'u_i': 2.3203},
        {'id': 4, 'e_m': 3.257255, 'e_o_k': [0.400482, 0.320386, 0.256309], 'p_i': 80, 'u_i': 3.8723},
        {'id': 5, 'e_m': 1.792700, 'e_o_k': [0.182185, 0.145748, 0.116598, 0.093279], 'p_i': 40, 'u_i': 1.1816},
        {'id': 6, 'e_m': 14.597411, 'e_o_k': [1.187013, 0.949610, 0.759688, 0.607751, 0.486201, 0.388960], 'p_i': 80, 'u_i': 4.5942},
        {'id': 7, 'e_m': 1.223941, 'e_o_k': [0.109228, 0.087383, 0.069906, 0.055925, 0.044740], 'p_i': 10, 'u_i': 3.3631},
    ]
    B_BUDGET = 95.679997
    return processors, tasks, B_BUDGET
