"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.572605, 'e_o_k': [0.159057, 0.127246], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 0.565553, 'e_o_k': [0.157098, 0.125678], 'p_i': 20, 'u_i': 4.7220},
        {'id': 2, 'e_m': 0.817880, 'e_o_k': [0.227189, 0.181751], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 5.124820, 'e_o_k': [1.423561, 1.138849], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 2.116956, 'e_o_k': [0.588043, 0.470435], 'p_i': 20, 'u_i': 3.9894},
        {'id': 5, 'e_m': 0.218732, 'e_o_k': [0.060759, 0.048607], 'p_i': 10, 'u_i': 1.1602},
        {'id': 6, 'e_m': 1.046970, 'e_o_k': [0.290825, 0.232660], 'p_i': 20, 'u_i': 4.5224},
        {'id': 7, 'e_m': 3.990809, 'e_o_k': [1.108558, 0.886847], 'p_i': 80, 'u_i': 3.6370},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET
