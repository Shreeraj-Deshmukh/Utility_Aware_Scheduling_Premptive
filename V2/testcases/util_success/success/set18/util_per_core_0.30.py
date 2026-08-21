"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759994, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759994, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.747564, 'e_o_k': [0.066715, 0.053372, 0.042698, 0.034158, 0.027326], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 0.445515, 'e_o_k': [0.054776, 0.043821, 0.035057], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 1.336910, 'e_o_k': [0.119310, 0.095448, 0.076358, 0.061087, 0.048869], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 3.494265, 'e_o_k': [0.311839, 0.249472, 0.199577, 0.159662, 0.127729], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 0.655670, 'e_o_k': [0.053317, 0.042654, 0.034123, 0.027298, 0.021839, 0.017471], 'p_i': 20, 'u_i': 3.3809},
        {'id': 5, 'e_m': 13.743922, 'e_o_k': [1.396740, 1.117392, 0.893914, 0.715131], 'p_i': 80, 'u_i': 4.9290},
        {'id': 6, 'e_m': 1.164911, 'e_o_k': [0.194152, 0.155321], 'p_i': 20, 'u_i': 1.8035},
        {'id': 7, 'e_m': 1.630387, 'e_o_k': [0.165690, 0.132552, 0.106041, 0.084833], 'p_i': 10, 'u_i': 3.4846},
    ]
    B_BUDGET = 71.759994
    return processors, tasks, B_BUDGET
