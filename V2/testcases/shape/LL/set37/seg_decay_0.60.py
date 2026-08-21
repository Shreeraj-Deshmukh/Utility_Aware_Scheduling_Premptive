"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199988, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199988, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.190797, 'e_o_k': [0.372124, 0.223274], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.359142, 'e_o_k': [0.082524, 0.049514, 0.029708, 0.017825], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 0.831853, 'e_o_k': [0.180398, 0.108239, 0.064943, 0.038966, 0.023380], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 10.420760, 'e_o_k': [2.394476, 1.436686, 0.862011, 0.517207], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 0.657127, 'e_o_k': [0.205352, 0.123211], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.368053, 'e_o_k': [0.079817, 0.047890, 0.028734, 0.017241, 0.010344], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 0.634198, 'e_o_k': [0.161785, 0.097071, 0.058243], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 0.421433, 'e_o_k': [0.091393, 0.054836, 0.032902, 0.019741, 0.011845], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 55.199988
    return processors, tasks, B_BUDGET
