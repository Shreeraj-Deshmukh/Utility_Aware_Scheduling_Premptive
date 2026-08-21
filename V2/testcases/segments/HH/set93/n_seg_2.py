"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.145211, 'e_o_k': [0.890719, 0.712576], 'p_i': 10, 'u_i': 1.6225},
        {'id': 1, 'e_m': 1.131105, 'e_o_k': [0.879748, 0.703799], 'p_i': 20, 'u_i': 4.7220},
        {'id': 2, 'e_m': 1.635759, 'e_o_k': [1.272257, 1.017806], 'p_i': 40, 'u_i': 1.8233},
        {'id': 3, 'e_m': 10.249639, 'e_o_k': [7.971942, 6.377553], 'p_i': 80, 'u_i': 1.9473},
        {'id': 4, 'e_m': 4.233912, 'e_o_k': [3.293042, 2.634434], 'p_i': 20, 'u_i': 3.9894},
        {'id': 5, 'e_m': 0.437464, 'e_o_k': [0.340250, 0.272200], 'p_i': 10, 'u_i': 1.1602},
        {'id': 6, 'e_m': 2.093940, 'e_o_k': [1.628620, 1.302896], 'p_i': 20, 'u_i': 4.5224},
        {'id': 7, 'e_m': 7.981619, 'e_o_k': [6.207926, 4.966340], 'p_i': 80, 'u_i': 3.6370},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET
