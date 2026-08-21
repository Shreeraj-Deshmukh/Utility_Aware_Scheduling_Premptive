"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.583594, 'e_o_k': [0.059308, 0.047447, 0.037957, 0.030366], 'p_i': 10, 'u_i': 1.2652},
        {'id': 1, 'e_m': 1.343459, 'e_o_k': [0.109246, 0.087397, 0.069917, 0.055934, 0.044747, 0.035798], 'p_i': 20, 'u_i': 2.0660},
        {'id': 2, 'e_m': 0.016444, 'e_o_k': [0.002741, 0.002193], 'p_i': 40, 'u_i': 3.5059},
        {'id': 3, 'e_m': 7.357529, 'e_o_k': [0.904614, 0.723691, 0.578953], 'p_i': 80, 'u_i': 1.7742},
        {'id': 4, 'e_m': 13.279599, 'e_o_k': [1.632738, 1.306190, 1.044952], 'p_i': 40, 'u_i': 1.4108},
        {'id': 5, 'e_m': 0.055574, 'e_o_k': [0.005648, 0.004518, 0.003615, 0.002892], 'p_i': 40, 'u_i': 2.2719},
        {'id': 6, 'e_m': 2.261591, 'e_o_k': [0.201832, 0.161465, 0.129172, 0.103338, 0.082670], 'p_i': 80, 'u_i': 4.1261},
        {'id': 7, 'e_m': 1.635060, 'e_o_k': [0.166165, 0.132932, 0.106345, 0.085076], 'p_i': 80, 'u_i': 2.8820},
    ]
    B_BUDGET = 71.760010
    return processors, tasks, B_BUDGET
