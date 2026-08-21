"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200013, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200013, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.118887, 'e_o_k': [0.024362, 0.019490, 0.015592], 'p_i': 10, 'u_i': 4.9795},
        {'id': 1, 'e_m': 1.151598, 'e_o_k': [0.235983, 0.188787, 0.151029], 'p_i': 20, 'u_i': 4.9448},
        {'id': 2, 'e_m': 3.783719, 'e_o_k': [0.775352, 0.620282, 0.496225], 'p_i': 40, 'u_i': 4.4554},
        {'id': 3, 'e_m': 10.046518, 'e_o_k': [2.058713, 1.646970, 1.317576], 'p_i': 80, 'u_i': 2.2591},
        {'id': 4, 'e_m': 0.109786, 'e_o_k': [0.022497, 0.017998, 0.014398], 'p_i': 10, 'u_i': 2.7803},
        {'id': 5, 'e_m': 4.986259, 'e_o_k': [1.021774, 0.817419, 0.653936], 'p_i': 80, 'u_i': 1.7696},
        {'id': 6, 'e_m': 1.553502, 'e_o_k': [0.318341, 0.254673, 0.203738], 'p_i': 80, 'u_i': 4.8086},
        {'id': 7, 'e_m': 0.352628, 'e_o_k': [0.072260, 0.057808, 0.046246], 'p_i': 20, 'u_i': 1.4894},
    ]
    B_BUDGET = 55.200013
    return processors, tasks, B_BUDGET
