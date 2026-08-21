"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320001, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.485314, 'e_o_k': [0.278459, 0.222767, 0.178214], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 1.461505, 'e_o_k': [0.838569, 0.670855, 0.536684], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 0.554952, 'e_o_k': [0.318415, 0.254732, 0.203786], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 1.824306, 'e_o_k': [1.046733, 0.837386, 0.669909], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 0.517558, 'e_o_k': [0.296959, 0.237568, 0.190054], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 5.062609, 'e_o_k': [2.904776, 2.323821, 1.859057], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 2.445941, 'e_o_k': [1.403409, 1.122727, 0.898182], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.179690, 'e_o_k': [0.103101, 0.082481, 0.065985], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 88.320001
    return processors, tasks, B_BUDGET
