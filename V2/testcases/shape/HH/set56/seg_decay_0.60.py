"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.150064, 'e_o_k': [1.262961, 0.757776, 0.454666, 0.272799, 0.163680, 0.098208], 'p_i': 10, 'u_i': 3.8590},
        {'id': 1, 'e_m': 0.276887, 'e_o_k': [0.168130, 0.100878, 0.060527, 0.036316, 0.021790], 'p_i': 20, 'u_i': 3.6983},
        {'id': 2, 'e_m': 1.036903, 'e_o_k': [0.629625, 0.377775, 0.226665, 0.135999, 0.081599], 'p_i': 40, 'u_i': 3.0670},
        {'id': 3, 'e_m': 0.261660, 'e_o_k': [0.228953, 0.137372], 'p_i': 80, 'u_i': 2.2547},
        {'id': 4, 'e_m': 12.654356, 'e_o_k': [11.072561, 6.643537], 'p_i': 80, 'u_i': 3.3628},
        {'id': 5, 'e_m': 0.168799, 'e_o_k': [0.147699, 0.088620], 'p_i': 10, 'u_i': 1.9431},
        {'id': 6, 'e_m': 2.612506, 'e_o_k': [1.586359, 0.951815, 0.571089, 0.342653, 0.205592], 'p_i': 80, 'u_i': 4.2381},
        {'id': 7, 'e_m': 3.342402, 'e_o_k': [2.387430, 1.432458, 0.859475], 'p_i': 10, 'u_i': 1.5683},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET
