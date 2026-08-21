"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520005, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520005, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1080, "set": 80, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.384952, 'e_o_k': [0.047330, 0.037864, 0.030291], 'p_i': 10, 'u_i': 2.2542},
        {'id': 1, 'e_m': 0.810114, 'e_o_k': [0.065876, 0.052701, 0.042161, 0.033728, 0.026983, 0.021586], 'p_i': 20, 'u_i': 3.1493},
        {'id': 2, 'e_m': 1.138107, 'e_o_k': [0.115661, 0.092529, 0.074023, 0.059219], 'p_i': 40, 'u_i': 4.3022},
        {'id': 3, 'e_m': 24.294908, 'e_o_k': [1.975581, 1.580465, 1.264372, 1.011498, 0.809198, 0.647358], 'p_i': 80, 'u_i': 4.8493},
        {'id': 4, 'e_m': 15.196782, 'e_o_k': [2.532797, 2.026238], 'p_i': 40, 'u_i': 1.1754},
        {'id': 5, 'e_m': 9.127415, 'e_o_k': [0.742211, 0.593769, 0.475015, 0.380012, 0.304010, 0.243208], 'p_i': 40, 'u_i': 3.0798},
        {'id': 6, 'e_m': 1.237859, 'e_o_k': [0.152196, 0.121757, 0.097405], 'p_i': 10, 'u_i': 3.4237},
        {'id': 7, 'e_m': 1.139385, 'e_o_k': [0.092651, 0.074121, 0.059297, 0.047437, 0.037950, 0.030360], 'p_i': 20, 'u_i': 3.1726},
    ]
    B_BUDGET = 143.520005
    return processors, tasks, B_BUDGET
