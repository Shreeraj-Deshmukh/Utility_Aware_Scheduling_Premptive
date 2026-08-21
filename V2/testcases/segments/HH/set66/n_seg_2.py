"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.134282, 'e_o_k': [0.104441, 0.083553], 'p_i': 10, 'u_i': 3.0491},
        {'id': 1, 'e_m': 1.595105, 'e_o_k': [1.240638, 0.992510], 'p_i': 20, 'u_i': 3.9469},
        {'id': 2, 'e_m': 4.086998, 'e_o_k': [3.178776, 2.543021], 'p_i': 40, 'u_i': 1.2331},
        {'id': 3, 'e_m': 10.112241, 'e_o_k': [7.865076, 6.292061], 'p_i': 80, 'u_i': 3.8857},
        {'id': 4, 'e_m': 1.915959, 'e_o_k': [1.490191, 1.192153], 'p_i': 20, 'u_i': 4.4773},
        {'id': 5, 'e_m': 1.005364, 'e_o_k': [0.781950, 0.625560], 'p_i': 10, 'u_i': 2.4546},
        {'id': 6, 'e_m': 1.093498, 'e_o_k': [0.850499, 0.680399], 'p_i': 80, 'u_i': 1.1544},
        {'id': 7, 'e_m': 21.458838, 'e_o_k': [16.690207, 13.352166], 'p_i': 80, 'u_i': 4.0204},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET
