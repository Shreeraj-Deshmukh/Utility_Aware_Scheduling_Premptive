"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.181209, 'e_o_k': [0.247803, 0.148682, 0.089209, 0.053526, 0.032115, 0.019269], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 0.909186, 'e_o_k': [0.231935, 0.139161, 0.083497], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 1.009200, 'e_o_k': [0.257449, 0.154469, 0.092682], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 5.488802, 'e_o_k': [1.400205, 0.840123, 0.504074], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 2.719998, 'e_o_k': [0.589868, 0.353921, 0.212352, 0.127411, 0.076447], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.142051, 'e_o_k': [0.032640, 0.019584, 0.011751, 0.007050], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 0.727869, 'e_o_k': [0.227459, 0.136475], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 3.047121, 'e_o_k': [0.700166, 0.420099, 0.252060, 0.151236], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET
