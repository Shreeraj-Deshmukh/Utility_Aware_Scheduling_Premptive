"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360014, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360014, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.647846, 'e_o_k': [0.052681, 0.042145, 0.033716, 0.026973, 0.021578, 0.017262], 'p_i': 10, 'u_i': 4.3913},
        {'id': 1, 'e_m': 1.355773, 'e_o_k': [0.225962, 0.180770], 'p_i': 20, 'u_i': 2.4366},
        {'id': 2, 'e_m': 14.901886, 'e_o_k': [1.211772, 0.969417, 0.775534, 0.620427, 0.496342, 0.397073], 'p_i': 40, 'u_i': 1.2704},
        {'id': 3, 'e_m': 6.403698, 'e_o_k': [0.650782, 0.520626, 0.416501, 0.333201], 'p_i': 80, 'u_i': 1.1761},
        {'id': 4, 'e_m': 13.602817, 'e_o_k': [2.267136, 1.813709], 'p_i': 40, 'u_i': 1.8297},
        {'id': 5, 'e_m': 9.553326, 'e_o_k': [1.592221, 1.273777], 'p_i': 20, 'u_i': 4.5821},
        {'id': 6, 'e_m': 4.515478, 'e_o_k': [0.752580, 0.602064], 'p_i': 40, 'u_i': 3.3407},
        {'id': 7, 'e_m': 3.368388, 'e_o_k': [0.342316, 0.273853, 0.219082, 0.175266], 'p_i': 40, 'u_i': 3.3443},
    ]
    B_BUDGET = 191.360014
    return processors, tasks, B_BUDGET
